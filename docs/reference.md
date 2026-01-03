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
usage: bpr [-e EXCLUDE] [-i INCLUDE] [-s] [-u] [-v] [-C] [-V] [-D] [-h] [package]  # (1)!

example: bpr [package]

positional arguments:
  package               Package name or file path

options:
  -e, --exclude EXCLUDE
                        Exclude regex patterns [CSV]
  -i, --include INCLUDE
                        Include regex patterns [CSV]
  -s, --single          Process single package
  -u, --url             Generate url [implies --single]
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

Process a single resource with `--single`.

```shell
bpr sharex-cli -s
```

Generate the `url` and `sha256` stanza with `--url`.

```shell
bpr brew-python-resources -u
```

```text
url "https://files.pythonhosted.org/packages/02/b4/7a80261f399e7a0b1611acb4056d485c3734edc7ff625e61470972e3127c/brew_python_resources-0.0.2.tar.gz"
sha256 "44719069bc244bf33806d15dcfa3a9acd43a3abe2f810c1b94e953495cdcf729"
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

??? note "Example: bpr -v brew-python-resources"

    ```text
    bpr -v brew-python-resources
    state={'verbose': 1}
    Package: brew-python-resources
    Package Name: brew-python-resources
    Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)]
    pip install brew-python-resources --quiet --dry-run --ignore-installed --report -
    --- COPY RESOURCES BELOW HERE -----------------------------------------------------------

      resource "attrs" do
        url "https://files.pythonhosted.org/packages/6b/5c/685e6633917e101e5dcb62b9dd76946cbb57c26e133bae9e0cd36033c0a9/attrs-25.4.0.tar.gz"
        sha256 "16d5969b87f0859ef33a48b35d55ac1be6e42ae49d5e853b597db70c35c57e11"
      end

      resource "cattrs" do
        url "https://files.pythonhosted.org/packages/6e/00/2432bb2d445b39b5407f0a90e01b9a271475eea7caf913d7a86bcb956385/cattrs-25.3.0.tar.gz"
        sha256 "1ac88d9e5eda10436c4517e390a4142d88638fe682c436c93db7ce4a277b884a"
      end

      resource "certifi" do
        url "https://files.pythonhosted.org/packages/a2/8c/58f469717fa48465e4a50c014a0400602d3c437d7c0c468e17ada824da3a/certifi-2025.11.12.tar.gz"
        sha256 "d8ab5478f2ecd78af242878415affce761ca6bc54a22a27e026d7c25357c3316"
      end

      resource "charset-normalizer" do
        url "https://files.pythonhosted.org/packages/13/69/33ddede1939fdd074bce5434295f38fae7136463422fe4fd3e0e89b98062/charset_normalizer-3.4.4.tar.gz"
        sha256 "94537985111c35f28720e43603b8e7b43a6ecfb2ce1d3058bbe955b73404e21a"
      end

      resource "idna" do
        url "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz"
        sha256 "795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902"
      end

      resource "pip" do
        url "https://files.pythonhosted.org/packages/fe/6e/74a3f0179a4a73a53d66ce57fdb4de0080a8baa1de0063de206d6167acc2/pip-25.3.tar.gz"
        sha256 "8d0538dbbd7babbd207f261ed969c65de439f6bc9e5dbd3b3b9a77f25d95f343"
      end

      resource "platformdirs" do
        url "https://files.pythonhosted.org/packages/cf/86/0248f086a84f01b37aaec0fa567b397df1a119f73c16f6c7a9aac73ea309/platformdirs-4.5.1.tar.gz"
        sha256 "61d5cdcc6065745cdd94f0f878977f8de9437be93de97c1c12f853c9c0cdcbda"
      end

      resource "requests" do
        url "https://files.pythonhosted.org/packages/c9/74/b3ff8e6c8446842c3f5c837e9c3dfcfe2018ea6ecef224c710c85ef728f4/requests-2.32.5.tar.gz"
        sha256 "dbba0bac56e100853db0ea71b82b4dfd5fe2bf6d3754a8893c3af500cec7d7cf"
      end

      resource "requests-cache" do
        url "https://files.pythonhosted.org/packages/1a/be/7b2a95a9e7a7c3e774e43d067c51244e61dea8b120ae2deff7089a93fb2b/requests_cache-1.2.1.tar.gz"
        sha256 "68abc986fdc5b8d0911318fbb5f7c80eebcd4d01bfacc6685ecf8876052511d1"
      end

      resource "typing_extensions" do
        url "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz"
        sha256 "0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"
      end

      resource "url-normalize" do
        url "https://files.pythonhosted.org/packages/80/31/febb777441e5fcdaacb4522316bf2a527c44551430a4873b052d545e3279/url_normalize-2.2.1.tar.gz"
        sha256 "74a540a3b6eba1d95bdc610c24f2c0141639f3ba903501e61a52a8730247ff37"
      end

      resource "urllib3" do
        url "https://files.pythonhosted.org/packages/1e/24/a2a2ed9addd907787d7aa0355ba36a6cadf1768b934c652ea78acbd59dcd/urllib3-2.6.2.tar.gz"
        sha256 "016f9c98bb7e98085cb2b4b17b87d2c702975664e4f060c6532e64d1c1a5e797"
      end

    --- COPY RESOURCES ABOVE HERE -----------------------------------------------------------
    ```

## :lucide-list: Environment

Many options support setting environment variable defaults.

| Variable      | Default |  Type  | Description                 |
| :------------ | :-----: | :----: | :-------------------------- |
| `BPR_PACKAGE` |    -    | `str`  | Package name or file        |
| `BPR_EXCLUDE` |    -    | `str`  | Exclude regex (CSV)         |
| `BPR_INCLUDE` |    -    | `str`  | Include regex (CSV)         |
| `BPR_SINGLE`  |    0    | `bool` | Process single resource     |
| `BPR_URL`     |    0    | `bool` | Generate `url` and `sha256` |
| `BPR_VERBOSE` |    0    | `int`  | Enable verbose output       |

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
