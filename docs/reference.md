---
icon: lucide/notebook-pen
---

# :lucide-notebook-pen: Reference

[![Brew Python Resources](assets/images/logo.svg){ align=right width=96 }](https://github.com/cssnr/brew-python-resources?tab=readme-ov-file#readme)

- [Install](#install)
- [Usage](#usage)
- [Environment](#environment)

The CLI executable is `bpr` or `brew-python-resources`.

The help is available with `--help`.

```shell
usage: bpr [-e EXCLUDE] [-i INCLUDE] [-s] [-v] [-C] [-V] [-D] [-h] [package]  # (1)!

example: bpr [package]

positional arguments:
  package               Package name or file path

options:
  -e, --exclude EXCLUDE
                        Exclude regex patterns [CSV]
  -i, --include INCLUDE
                        Include regex patterns [CSV]
  -s, --single          Process single package
  -v, --verbose         Verbose output [debug: -vvv]
  -C, --clear-cache     Clear request cache
  -V, --version         Show installed version
  -D, --docs            Launch docs in browser
  -h, --help            Show this help message
```

1. :lucide-lightbulb: Tip: Save your options with [Environment Variables](#environment).

To view the source code, see the [cli.py :lucide-arrow-up-right:](https://github.com/cssnr/brew-python-resources/blob/master/src/brewresources/cli.py) on GitHub.

_Note: `single` should not be used with `exclude` or `include`._

## :simple-pypi: Install

From [PyPI :lucide-arrow-up-right:](https://pypi.org/p/brew-python-resources),
[Homebrew :lucide-arrow-up-right:](https://github.com/cssnr/homebrew-tap?tab=readme-ov-file#readme)
or [GitHub :lucide-arrow-up-right:](https://github.com/cssnr/brew-python-resources/releases/latest).

=== "uv"

    ```shell
    uv tool install brew-python-resources
    ```

=== "pip"

    ```shell
    pip install brew-python-resources
    ```

=== "brew"

    ```shell
    brew install cssnr/tap/brew-python-resources
    ```

=== "release"

    ```shell
    curl https://i.jpillora.com/cssnr/sharex-cli! | bash  # (1)!
    ```

    1.  Note: the `!` installs into `/usr/local/bin`.

        Omit this to use the current directory.

        See [jpillora/installer :lucide-arrow-up-right:](https://github.com/jpillora/installer) for more details.

Upgrade.

=== "uv"

    ```shell
    uv tool upgrade brew-python-resources
    ```

=== "pip"

    ```shell
    pip install -U brew-python-resources
    ```

=== "brew"

    ```shell
    brew update && brew install brew-python-resources
    ```

=== "release"

    ```shell
    curl https://i.jpillora.com/cssnr/sharex-cli! | bash  # (1)!
    ```

    1.  To upgrade, re-install the latest release.

Uninstall.

=== "uv"

    ```shell
    uv tool uninstall brew-python-resources
    ```

=== "pip"

    ```shell
    pip uninstall brew-python-resources
    ```

=== "brew"

    ```shell
    brew uninstall brew-python-resources
    ```

=== "release"

    ```shell
    rm -f /usr/local/bin/sharex  # (1)!
    ```

    1.  If you used the installation script above.

Run without installing using [astral-sh/uv :lucide-arrow-up-right:](https://docs.astral.sh/uv/).

```shell
uvx brew-python-resources
```

Check the installed `--version`.

```shell
bpr -V
```

## :lucide-square-terminal: Usage

The Python Version depends on the running interpreter.

```shell
python --version
```

To generate resources for a specific version, use that version.

```shell
uv venv --python 3.10
source .venv/bin/activate
python --version
```

The CLI executable is `bpr` or `brew-python-resources`.

Run on a published pacakge.

```shell
bpr sharex-cli
```

Run on a package file.

```shell
bpr dist/sharex-cli-0.0.1-py3-none-any.whl
```

Process a single resource.

```shell
bpr sharex-cli -s
```

Exclude or include packages with regex. Comma seperated list of patterns.

```shell
bpr sharex-cli -e "colorama"
bpr sharex-cli -i "click,requests,typer"
```

Increase output with `--verbose`. Debug with `-vv` or `-vvv`.

```shell
bpr sharex-cli -v
```

Output results to a file.

```shell
bpr sharex-cli > output.txt
```

Run without installing using [astral-sh/uv :lucide-arrow-up-right:](https://docs.astral.sh/uv/).

```shell
uvx brew-python-resources sharex-cli
```

Example (verbose output).

```text
$ bpr -v toml-run
Package: toml-run
Python 3.8.20 (default, Oct  2 2024, 16:34:12)
--- COPY RESOURCES BELOW HERE -----------------------------------------------------------------------

  resource "tomli" do
    url "https://files.pythonhosted.org/packages/52/ed/3f73f72945444548f33eba9a87fc7a6e969915e7b1acc8260b30e1f76a2f/tomli-2.3.0.tar.gz"
    sha256 "64be704a875d2a59753d80ee8a533c3fe183e3f06807ff7dc2232938ccb01549"
  end

--- COPY RESOURCES ABOVE HERE -----------------------------------------------------------------------
```

Note: verbose outputs to stderr so you can still capture the resources with stdout.

## :lucide-list: Environment

Many options support setting environment variable defaults.

| Environment&nbsp;Variable | Default |  Type  | Description           |
| :------------------------ | :-----: | :----: | :-------------------- |
| `BPR_PACKAGE`             |    -    | `str`  | Package name or file  |
| `BPR_EXCLUDE`             |    -    | `str`  | Exclude regex         |
| `BPR_INCLUDE`             |    -    | `str`  | Include regex         |
| `BPR_SINGLE`              |    0    | `bool` | Single resource       |
| `BPR_VERBOSE`             |    0    | `int`  | Enable verbose output |

Allowed boolean values, case-insensitive.

```plain
0, f, n, no, off, false
1, t, y, on, yes, true
```

You can temporarily set variables on the command line.

=== "Unix"

    ```shell
    export BPR_VERBOSE=1
    ```

=== "Windows"

    ```pwsh
    $env:BPR_VERBOSE=1
    ```

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
