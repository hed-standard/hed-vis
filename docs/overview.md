---
myst:
  html_meta:
    description: HED visualization overview - Introduction to hedvis for creating word clouds and visual summaries
    keywords: HED visualization, hedvis overview, word cloud generation, HED tools, neuroscience visualization
---

```{index} visualization; HED
```

```{index} word cloud
```

```{index} hedvis
```

# HED visualization overview

**hedvis** (HED Visualization Tools) is a Python package that provides visualization utilities for {index}`HED (Hierarchical Event Descriptors)` annotated datasets. It focuses specifically on creating {index}`word clouds <word cloud>` and {index}`visual summaries <visualization>` from HED tag data.

This package is a companion library to [hedtools](https://github.com/hed-standard/hed-python), the core HED Python tools package. While hedtools handles HED schema management, validation, and data processing, hedvis provides specialized visualization capabilities.

```{index} tag frequency
```

```{index} patterns; visualization
```

## Why use hedvis?

{index}`HED-annotated datasets <dataset; HED-annotated>` contain rich semantic information about events and experimental conditions. hedvis makes it easy to:

- **Visualize tag frequency** - Create word clouds showing which {index}`HED tags <tag; HED>` are most commonly used
- **Identify patterns** - Quickly spot dominant tags and {index}`event types <event>` in your data
- **Generate reports** - Produce {index}`publication-ready visualizations <visualization; publication-ready>`
- **Explore datasets** - Get a quick visual overview of what's in your data

```{index} mask image
```

```{index} colormap
```

```{index} PNG format
```

```{index} SVG format
```

## Key hedvis features

### Word cloud generation

- Create customizable word clouds from {index}`HED tag frequencies <tag frequency>`
- Support for {index}`shaped clouds <word cloud; shaped>` using {index}`mask images <mask image>`
- Flexible {index}`color schemes <colormap>` and layouts
- Export to {index}`PNG <PNG format>` and {index}`SVG <SVG format>` formats

```{index} hedtools
```

```{index} BIDS dataset
```

```{index} tag template
```

```{index} HedTagVisualizer
```

### Integration with hedtools

- Works seamlessly with {index}`hedtools` data structures
- Process data from {index}`BIDS datasets <BIDS dataset>`, {index}`spreadsheets <tabular data>`, or {index}`dataframes <pandas DataFrame>`
- Automatic {index}`tag frequency counting <tag frequency>`
- Support for {index}`tag templates <tag template>` and {index}`filtering <tag; filtering>`

### Two APIs for flexibility

- **New API** - Modern, {index}`configuration-based interface <VisualizationConfig>` using {index}`HedTagVisualizer`
- **Legacy API** - Simple {index}`functional interface <API; legacy>` for quick word cloud generation

## Installing hedvis

```{index} installation
```

```{index} PyPI
```

Install from PyPI:

```bash
pip install hedvis
```

This automatically installs hedtools and all required dependencies.

### Installing with Optional Dependencies

```{index} dependencies; optional
```

```{index} pip extras
```

```{index} pyproject.toml
```

**All dependencies are managed in `pyproject.toml`.** Install optional extras as needed.

**Important:** Installing with extras automatically includes all base dependencies (hedtools, numpy, pandas, matplotlib, etc.) plus the extra tools.

**Key distinction:**

- Use `"hedvis[extra]"` when installing from **PyPI** (the published package)
- Use `".[extra]"` when installing from **local source** (after cloning the repository)

```bash
# Development tools (formatting, linting, testing)
# From PyPI
pip install "hedvis[dev]"
# From local source
pip install ".[dev]"          # Regular install
pip install -e ".[dev]"       # Editable install (recommended for development)

# Documentation tools (Sphinx, themes)
# From PyPI
pip install "hedvis[docs]"
# From local source
pip install ".[docs]"

# Both dev and docs dependencies
# From PyPI
pip install "hedvis[dev,docs]"
# From local source
pip install ".[dev,docs]"
```

For development work (clone and install in editable mode):

```bash
git clone https://github.com/hed-standard/hed-vis.git
cd hed-vis
pip install -e ".[dev]"
```

Install directly from the [GitHub repository](https://github.com/hed-standard/hed-vis):

```bash
pip install git+https://github.com/hed-standard/hed-vis.git
```

**Note:** All dependencies are defined in `pyproject.toml`. Legacy requirements files (`requirements.txt`, `requirements-dev.txt`, `docs/requirements.txt`) are deprecated and will be removed in a future release.

## Quick example

```{index} quick start
```

```{index} examples
```

```python
from hedvis import HedTagVisualizer

# Create visualizer with default configuration
visualizer = HedTagVisualizer()

# Visualize from pre-computed tag counts (from hedtools)
results = visualizer.visualize_from_counts(tag_counts)

# Save word cloud
results['word_cloud']['wordcloud_object'].to_file('output.png')
```

## Related projects

```{index} related projects
```

```{index} hed-python
```

```{index} hed-schemas
```

- **[hed-python](https://github.com/hed-standard/hed-python)**: Core HED Python tools for validation, schema management, and analysis
- **[hed-schemas](https://github.com/hed-standard/hed-schemas)**: Official HED schemas in multiple formats
- **[table-remodeler](https://github.com/hed-standard/table-remodeler)**: Python tools for manipulating and restructuring tables

## Finding help

```{index} help
```

```{index} support
```

### Documentation

```{index} documentation
```

- See this documentation for detailed usage guides and API reference
- Visit [HED resources](https://www.hedtags.org/hed-resources) for general HED documentation
- Check the [Python hedtools documentation](https://www.hedtags.org/hed-python) for core HED functionality

### Issues and problems

```{index} issues
```

```{index} bug reports
```

If you encounter bugs or have feature requests:

- **hedvis issues**: [open an issue](https://github.com/hed-standard/hed-vis/issues) in the hed-vis repository
- **hedtools issues**: [open an issue](https://github.com/hed-standard/hed-python/issues) in the hed-python repository
- **Questions or ideas**: [HED organization discussions][HED organization discussions](https://github.com/orgs/hed-standard/discussions)
- **Contact**: [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
