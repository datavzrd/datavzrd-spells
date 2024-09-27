# datavzrd-spells

This repository is designed to provide reusable configuration snippets, or "spells," for [datavzrd](https://github.com/datavzrd/datavzrd). These spells simplify the process of creating reports by allowing users to define common configurations in a modular way. Users can easily pull spells from local files or remote URLs, facilitating consistency and efficiency in data visualization workflows. The repository supports various statistical and visual functions, empowering data scientists, analysts, and developers to create insightful and aesthetically pleasing visualizations with minimal effort.

### Usage

This basic example uses a spell for a p-value visualization:

```yaml
render-table:
  columns:
    p-value:
      spell:
        url: "https://github.com/datavzrd/datavzrd-spells/raw/main/stats/p-value/spell.yaml"
        with:
          significance_threshold: 0.05
```

In this example, the p-value column uses a spell that is fetched from the repository, allowing you to specify a significance threshold.
