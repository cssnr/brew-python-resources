[![PyPI Version](https://img.shields.io/pypi/v/brew-python-resources?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/brew-python-resources/)
[![GitHub Release Version](https://img.shields.io/github/v/release/cssnr/brew-python-resources?logo=github)](https://github.com/cssnr/brew-python-resources/releases)
[![TOML Python Version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2Fcssnr%2Fbrew-python-resources%2Frefs%2Fheads%2Fmaster%2Fpyproject.toml&query=%24.project.requires-python&logo=python&logoColor=white&label=python)](https://github.com/cssnr/brew-python-resources?tab=readme-ov-file#readme)
[![PyPI Downloads](https://img.shields.io/pypi/dm/brew-python-resources?logo=pypi&logoColor=white)](https://pypistats.org/packages/brew-python-resources)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/brew-python-resources?logo=pypi&logoColor=white&label=total)](https://clickpy.clickhouse.com/dashboard/brew-python-resources)
[![Codecov](https://codecov.io/gh/cssnr/brew-python-resources/graph/badge.svg?token=A8NDHZ393X)](https://codecov.io/gh/cssnr/brew-python-resources)
[![Workflow Lint](https://img.shields.io/github/actions/workflow/status/cssnr/brew-python-resources/lint.yaml?logo=cachet&label=lint)](https://github.com/cssnr/brew-python-resources/actions/workflows/lint.yaml)
[![Workflow Test](https://img.shields.io/github/actions/workflow/status/cssnr/brew-python-resources/test.yaml?logo=cachet&label=test)](https://github.com/cssnr/brew-python-resources/actions/workflows/test.yaml)
[![Deployment PyPi](https://img.shields.io/github/deployments/cssnr/brew-python-resources/pypi?logo=pypi&logoColor=white&label=pypi)](https://pypi.org/project/brew-python-resources/)
[![Deployment Docs](https://img.shields.io/github/deployments/cssnr/brew-python-resources/docs?logo=materialformkdocs&logoColor=white&label=docs)](https://cssnr.github.io/brew-python-resources/)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/cssnr/brew-python-resources?logo=github&label=updated)](https://github.com/cssnr/brew-python-resources/pulse)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/cssnr/brew-python-resources?logo=bookstack&logoColor=white&label=repo%20size)](https://github.com/cssnr/brew-python-resources)
[![GitHub Top Language](https://img.shields.io/github/languages/top/cssnr/brew-python-resources?logo=htmx&logoColor=white)](https://github.com/cssnr/brew-python-resources?tab=readme-ov-file#readme)
[![GitHub Contributors](https://img.shields.io/github/contributors-anon/cssnr/brew-python-resources?logo=github)](https://github.com/cssnr/brew-python-resources/graphs/contributors)
[![GitHub Issues](https://img.shields.io/github/issues/cssnr/brew-python-resources?logo=github)](https://github.com/cssnr/brew-python-resources/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/cssnr/brew-python-resources?logo=github)](https://github.com/cssnr/brew-python-resources/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/cssnr/brew-python-resources?style=flat&logo=github)](https://github.com/cssnr/brew-python-resources/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/cssnr/brew-python-resources?style=flat&logo=github)](https://github.com/cssnr/brew-python-resources/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=github&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

# Brew Python Resources

<a title="Brew Python Resources" href="https://cssnr.github.io/brew-python-resources/" target="_blank">
<img alt="Brew Python Resources" align="right" width="128" height="auto" src="https://cssnr.github.io/brew-python-resources/assets/images/logo.svg"></a>

- [Features](#features)
- [Install](#install)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

Generate and Update Homebrew Formula (Brew) Python Resources.

To get started [Install](#install) the cli and view the [Usage](#usage).

If you run into any issues or have any questions, [support](#support) is available.

[![View Documentation](https://img.shields.io/badge/view_documentation-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/brew-python-resources/)

## Features<a id="features"></a>

- Works on published packages or package files
- Include and Exclude regex or single resource
- Does not require Homebrew or formula files
- Does not create a venv or install packages
- Uses caching for repeated runs

[![View Full Reference](https://img.shields.io/badge/view_full_reference-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/brew-python-resources/reference/)

## Install<a id="install"></a>

From PyPI: <https://pypi.org/p/brew-python-resources>

```shell
pip install brew-python-resources
```

```shell
uv tool install brew-python-resources
```

From Homebrew: <https://github.com/cssnr/homebrew-tap>

```shell
brew install cssnr/tap/brew-python-resources
```

From GitHub: <https://github.com/cssnr/brew-python-resources/releases/latest>

```shell
curl https://i.jpillora.com/cssnr/brew-python-resources! | bash
```

See [jpillora/installer](https://github.com/jpillora/installer) for more details.  
Alternatively, you can manually download a release for your system.

- [Windows x86_64](https://github.com/cssnr/brew-python-resources/releases/latest/download/windows-amd64.zip) _amd64_
- [macOS Apple Intel](https://github.com/cssnr/brew-python-resources/releases/latest/download/macos-amd64.zip) _amd64_
- [macOS Apple Silicon](https://github.com/cssnr/brew-python-resources/releases/latest/download/macos-arm64.zip) _arm64_
- [Linux x86_64](https://github.com/cssnr/brew-python-resources/releases/latest/download/linux-amd64.zip) _amd64_
- [Linux ARM](https://github.com/cssnr/brew-python-resources/releases/latest/download/linux-arm64.zip) _arm64_

[![View Install Guide](https://img.shields.io/badge/view_install_guide-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/brew-python-resources/reference/#install)

## Usage<a id="usage"></a>

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

[![View Usage Guide](https://img.shields.io/badge/view_usage_guide-blue?style=for-the-badge&logo=googledocs&logoColor=white)](https://cssnr.github.io/brew-python-resources/reference/#usage)

## Support<a id="support"></a>

If you run into any issues or need help getting started, please do one of the following:

- Report an Issue: <https://github.com/cssnr/brew-python-resources/issues>
- Q&A Discussion: <https://github.com/cssnr/brew-python-resources/discussions/categories/q-a>
- Request a Feature: <https://github.com/cssnr/brew-python-resources/issues/new?template=1-feature.yaml>
- Chat with us on Discord: <https://discord.gg/wXy6m2X8wY>

[![Features](https://img.shields.io/badge/features-brightgreen?style=for-the-badge&logo=googleanalytics&logoColor=white)](https://github.com/cssnr/brew-python-resources/issues/new?template=1-feature.yaml)
[![Issues](https://img.shields.io/badge/issues-red?style=for-the-badge&logo=southwestairlines&logoColor=white)](https://github.com/cssnr/brew-python-resources/issues)
[![Discussions](https://img.shields.io/badge/discussions-blue?style=for-the-badge&logo=rocketdotchat&logoColor=white)](https://github.com/cssnr/brew-python-resources/discussions)
[![Discord](https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/wXy6m2X8wY)

## Contributing<a id="contributing"></a>

If you would like to submit a PR, please review the [CONTRIBUTING.md](#contributing-ov-file).

Please consider making a donation to support the development of this project
and [additional](https://cssnr.com/) open source projects.

[![Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/cssnr)

For a full list of current projects visit: [https://cssnr.github.io/](https://cssnr.github.io/)
