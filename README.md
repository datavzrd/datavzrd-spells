[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/datavzrd/datavzrd-spells/testing.yml?branch=main&label=tests)](https://github.com/datavzrd/datavzrd-spells/actions)
![GitHub Release](https://img.shields.io/github/v/release/datavzrd/datavzrd-spells)


# datavzrd-spells

This repository is designed to provide reusable configuration snippets, or _*spells*_, for [datavzrd](https://github.com/datavzrd/datavzrd). These spells simplify the process of creating reports by allowing users to define common configurations in a modular way. Users can easily pull spells from local files or remote URLs, facilitating consistency and efficiency in data visualization workflows. The repository supports various statistical and visual functions, empowering data scientists, analysts, and developers to create insightful and aesthetically pleasing visualizations with minimal effort.

A catalog of all available spells can be found at https://datavzrd.github.io/docs/spells.html.

# Contributing a new spell

New spells can be contributed by

1. Forking and cloning this repository.
2. Adding a spell subfolder (e.g. `stats/spellname`). Try to use speaking names that already explain what the spell visualizes.
3. Create a `meta.yaml`, a `spell.yaml` and a `tests` subfolder with appropriate content. Use the already available spells for inspiration.
4. Open a pull request. In the pull request, make sure to see whether the tests pass or complain, and check out the generated artifacts for the testcase output of your spell. Once the pull request is merged, your spell will automatically occur in the catalog at https://datavzrd.github.io/docs/spells.html.