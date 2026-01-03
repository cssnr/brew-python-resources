---
icon: lucide/rocket
---

# :lucide-rocket: Get Started

[![Brew Python Resources](assets/images/logo.svg){ align=right width=96 }](https://github.com/cssnr/brew-python-resources?tab=readme-ov-file#readme)

[![PyPI Version](https://img.shields.io/pypi/v/brew-python-resources?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/brew-python-resources/)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Fbrew-python-resources%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=python)](https://github.com/cssnr/brew-python-resources?tab=readme-ov-file#readme)
[![PyPI Downloads](https://img.shields.io/pypi/dm/brew-python-resources?logo=pypi&logoColor=white)](https://pypistats.org/packages/brew-python-resources)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/brew-python-resources?logo=pypi&logoColor=white&label=total)](https://clickpy.clickhouse.com/dashboard/brew-python-resources)
[![Codecov](https://codecov.io/gh/cssnr/brew-python-resources/graph/badge.svg?token=A8NDHZ393X)](https://codecov.io/gh/cssnr/brew-python-resources)
[![Workflow Test](https://img.shields.io/github/actions/workflow/status/cssnr/brew-python-resources/test.yaml?logo=cachet&label=test)](https://github.com/cssnr/brew-python-resources/actions/workflows/test.yaml)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/brew-python-resources?logo=github&label=updated)](https://github.com/cssnr/brew-python-resources/pulse)
[![GitHub Issues](https://img.shields.io/github/issues/cssnr/brew-python-resources?logo=github)](https://github.com/cssnr/brew-python-resources/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/brew-python-resources?logo=github)](https://github.com/cssnr/brew-python-resources/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/brew-python-resources?style=flat&logo=github)](https://github.com/cssnr/brew-python-resources/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/brew-python-resources?style=flat&logo=github)](https://github.com/cssnr/brew-python-resources/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

Generate and Update Homebrew Formula (Brew) Python Resources.

To get started see the [Quick Start](#quick-start) section or check out the [Features](#features).

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
    curl https://i.jpillora.com/cssnr/brew-python-resources! | bash  # (1)!
    ```

    1.  Note: the `!` installs into `/usr/local/bin`.

        Omit the `!` to use the current directory.

        See [jpillora/installer :lucide-arrow-up-right:](https://github.com/jpillora/installer) for more details.

If you run into any issues or have any questions, [support](support.md) is available.

!!! tip "There are detailed [Install](reference.md#install) and [Usage](reference.md#usage) guides available."

## :lucide-sparkles: Features

- Works on published packages or package files
- Include and Exclude regex or single resource
- Can generate a `url` and `sha256` stanza
- Does not require Homebrew or formula files
- Does not create a venv or install packages
- Does not require packages to be installed
- Uses requests cache for repeated runs

For more details see the [full reference](reference.md).

## :lucide-plane-takeoff: Quick Start

[Install](reference.md#install) from [PyPI :lucide-arrow-up-right:](https://pypi.org/p/brew-python-resources),
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
    curl https://i.jpillora.com/cssnr/brew-python-resources! | bash  # (1)!
    ```

    1.  Note: the `!` installs into `/usr/local/bin`.

        Omit the `!` to use the current directory.

        See [jpillora/installer :lucide-arrow-up-right:](https://github.com/jpillora/installer) for more details.

Run with.

```shell
bpr [package name or file]
```

Or, run without installing using [astral-sh/uv :lucide-arrow-up-right:](https://docs.astral.sh/uv/).

```shell
uvx brew-python-resources [package name or file]
```

[:simple-pypi: &nbsp; Install Guide](reference.md#install){ .md-button .md-button--primary }

[:lucide-square-terminal: &nbsp; Usage Guide](reference.md#usage){ .md-button .md-button--primary }

&nbsp;

!!! question

    If you need **help** getting started or run into any issues, [support](support.md) is available!
