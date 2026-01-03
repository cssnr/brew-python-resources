import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import webbrowser
from pathlib import Path
from typing import Any, List, Optional

from requests_cache import CachedSession

from ._version import __version__
from .utils import str_to_bool


docs = "https://cssnr.github.io/brew-python-resources/"
state = {"verbose": 0}
session = CachedSession("brew-python-resources", use_cache_dir=True, expire_after=3600)
os.environ["PYTHONIOENCODING"] = "utf-8"


class Package(object):
    def __init__(self, name: str, version: str):
        self.name = name.lower().strip()
        self.version = version.strip()

    def __repr__(self):
        return f"{self.name}@{self.version}"

    def __lt__(self, other):
        return self.name < other.name


class Resource(object):
    def __init__(self, name: str, url: str, sha256: str):
        self.name = name.lower().strip()
        self.url = url.strip()
        self.sha256 = sha256.strip()

    def __repr__(self):
        return os.path.basename(self.url)


class DocsAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):  # pragma: no cover
        result = webbrowser.open_new_tab(docs)
        if not result:
            raise ValueError(f"Unable to launch browser.\n\nVisit: {docs}\n")
        print(f"Launched: {docs}")
        raise SystemExit


class CacheAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):  # pragma: no cover
        session.cache.clear()
        print("Cache Cleared.")
        raise SystemExit


def vprint(*objects: Any, lvl=1, sep="\n", **kwargs):
    if state["verbose"] >= lvl:  # pragma: no cover
        print(*objects, file=sys.stderr, sep=sep, **kwargs)


def print_rule(title: str, lvl: int = 0, rule: str = "-", pre: int = 3, **kwargs):
    if state["verbose"] >= lvl:  # pragma: no cover
        width = shutil.get_terminal_size(fallback=(80, 24)).columns - 1
        text = f"{rule * pre} {title} "
        result = text + rule * (width - len(text))
        print(result[:width], **kwargs)


def env(name: str) -> Any:
    result = os.environ.get(f"BPR_{name}".upper())
    if name in ["single", "url"]:
        return str_to_bool(result)
    elif name == "verbose":
        return int(result) if result and result.isdigit() else 0
    else:
        return result


def run() -> None:
    parser = argparse.ArgumentParser(description="example: %(prog)s [package]", epilog=f"docs: {docs}", add_help=False)
    parser.add_argument("package", nargs="?", default=env("package"), help="Package name or file path")
    parser.add_argument("-e", "--exclude", default=env("exclude"), help="Exclude regex patterns [CSV]")
    parser.add_argument("-i", "--include", default=env("include"), help="Include regex patterns [CSV]")
    parser.add_argument("-s", "--single", action="store_true", default=env("single"), help="Process single package")
    parser.add_argument("-u", "--url", action="store_true", default=env("url"), help="Generate url [implies --single]")
    parser.add_argument("-v", "--verbose", action="count", default=env("verbose"), help="Verbose output [debug: -vvv]")
    parser.add_argument("-C", "--clear-cache", action=CacheAction, nargs=0, help="Clear request cache")
    parser.add_argument("-V", "--version", action="version", version=__version__, help="Show installed version")
    parser.add_argument("-D", "--docs", action=DocsAction, nargs=0, help="Launch docs in browser")
    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="Show this help message")
    args = parser.parse_args()
    state["verbose"] = args.verbose
    vprint(f"{state=}")
    vprint(f"{args=}", lvl=2)

    vprint(f"Package: {args.package}")
    if not args.package:
        # parser.print_help()
        raise ValueError("Package [name] is required. Use --help for more details.")

    package_name = args.package.lower()
    path = Path(args.package)
    if path.is_file():  # pragma: no cover
        vprint(f"Package File: {path.absolute()}")
        package_name = path.name.split("-")[0].lower()

    vprint(f"Package Name: {package_name}")
    vprint(f"Python {sys.version}")
    command = ["pip", "install", args.package, "--quiet", "--dry-run", "--ignore-installed", "--report", "-"]
    vprint(" ".join(command))

    output: bytes = subprocess.check_output(command)  # nosec
    data: dict = json.loads(output.decode())
    install: list = data.get("install", [])

    packages: List[Package] = sorted([Package(d["metadata"]["name"], d["metadata"]["version"]) for d in install])
    vprint(f"initial sorted ({len(packages)}): {packages=}", lvl=2)

    packages = [p for p in packages if cmp_package(p.name, package_name, args.single or args.url)]
    vprint(f"default filter ({len(packages)}): {packages=}", lvl=2)

    packages = filter_list(packages, args.include)
    packages = filter_list(packages, args.exclude, True)
    vprint(f"after excludes ({len(packages)}): {packages=}", lvl=2)

    resources = []
    for package in packages:
        print_rule(package.name, 2)
        url = get_url(package)
        if not url:  # pragma: no cover
            print(f"Warning: No URL for package: {package.name}", file=sys.stderr)
            continue
        vprint(f"{url=}", lvl=3)
        vprint(f"{url['url']=}", f"{url['digests']['sha256']=}", lvl=2)
        resources.append(Resource(package.name, url["url"], url["digests"]["sha256"]))
    print_rule("packages loop finished", 2)

    vprint(f"{resources=}", lvl=2)
    if not resources:
        raise ValueError(f"No dependencies found for: {args.package}")  # pragma: no cover

    print_rule("COPY RESOURCES BELOW HERE", 1, file=sys.stderr, end="\n\n")
    if args.url:
        print(f'  url "{resources[0].url}"', f'  sha256 "{resources[0].sha256}"', sep="\n", end="\n\n")
    else:
        for resource in resources:
            print(
                f'  resource "{resource.name}" do',
                f'    url "{resource.url}"',
                f'    sha256 "{resource.sha256}"',
                "  end\n",
                sep="\n",
            )
    print_rule("COPY RESOURCES ABOVE HERE", 1, file=sys.stderr)


def cmp_package(a: str, b: str, equals=True) -> bool:
    result = a.replace("_", "-") == b.replace("_", "-")
    return result if equals else not result


def filter_list(packages: List[Package], args: str, is_exclude: bool = False) -> list:  # NOSONAR: python:S3776
    if not args:
        return packages
    filtered_packages = packages.copy() if is_exclude else []
    for pattern in args.split(","):
        vprint(f"Processing {'exclude' if is_exclude else 'include'}: {pattern}")
        for package in packages:
            match = re.match(pattern, package.name, re.IGNORECASE)
            if is_exclude:
                if match:
                    filtered_packages.remove(package)
            else:
                if match:
                    filtered_packages.append(package)
    return filtered_packages


def get_url(package: Package) -> Optional[dict]:
    r = session.get(f"https://pypi.org/pypi/{package.name}/{package.version}/json")
    vprint(f"{r.url=}", f"{r.from_cache=}", lvl=2)
    data: dict = r.json()
    for url in data.get("urls", []):
        if url.get("packagetype") == "sdist":
            return url
    return None  # pragma: no cover


def main() -> None:
    try:
        run()
    except KeyboardInterrupt:
        sys.exit(1)  # pragma: no cover
    except Exception as error:
        print(f"\nError: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()  # pragma: no cover
