[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/datavzrd/datavzrd-spells/testing.yml?branch=main&label=tests)](https://github.com/datavzrd/datavzrd-spells/actions)

# datavzrd-spells

This repository is designed to provide reusable configuration snippets, or _*spells*_, for [datavzrd](https://github.com/datavzrd/datavzrd). These spells simplify the process of creating reports by allowing users to define common configurations in a modular way. Users can easily pull spells from local files or remote URLs, facilitating consistency and efficiency in data visualization workflows. The repository supports various statistical and visual functions, empowering data scientists, analysts, and developers to create insightful and aesthetically pleasing visualizations with minimal effort.

### Usage

This basic example uses a spell for a p-value visualization:

```yaml
render-table:
  columns:
    p-value:
      spell:
        url: "v1.0.0/stats/p-value"
        with:
          significance_threshold: 0.05
```

In this example, the p-value column uses a spell that is fetched from the repository, allowing you to specify a significance threshold. 
Spell can be used very flexible using any local file path, specific versioned URLs (e.g. `v1.0.0/stats/p-value`), or any remote URL like `https://github.com/datavzrd/datavzrd-spells/raw/main/stats/p-value/spell.yaml`.
