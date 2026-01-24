# Intro to HED visualization

## Overview

**hedvis** (HED Visualization Tools) is a Python package that provides visualization utilities for HED (Hierarchical Event Descriptors) annotated datasets. It focuses specifically on creating word clouds and visual summaries from HED tag data.

This package is a companion library to [hedtools](https://github.com/hed-standard/hed-python), the core HED Python tools package. While hedtools handles HED schema management, validation, and data processing, hedvis provides specialized visualization capabilities.

## Why use hedvis?

HED-annotated datasets contain rich semantic information about events and experimental conditions. hedvis makes it easy to:

- **Visualize tag frequency** - Create word clouds showing which HED tags are most commonly used
- **Identify patterns** - Quickly spot dominant tags and event types in your data
- **Generate reports** - Produce publication-ready visualizations of your HED annotations
- **Explore datasets** - Get a quick visual overview of what's in your data

## Key features

### Word cloud generation

- Create customizable word clouds from HED tag frequencies
- Support for shaped clouds using mask images
- Flexible color schemes and layouts
- Export to PNG and SVG formats

### Integration with hedtools

- Works seamlessly with hedtools data structures
- Process data from BIDS datasets, spreadsheets, or dataframes
- Automatic tag frequency counting
- Support for tag templates and filtering

### Two APIs for flexibility

- **New API** - Modern, configuration-based interface using `HedTagVisualizer`
- **Legacy API** - Simple functional interface for quick word cloud generation

## Installing hedvis

You can install hedvis from PyPI:

```bash
pip install hedvis
```

This will automatically install hedtools and other required dependencies.

Or install directly from the [GitHub repository](https://github.com/hed-standard/hed-vis):

```bash
pip install git+https://github.com/hed-standard/hed-vis.git
```

## Quick example

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

- **[hedtools](https://github.com/hed-standard/hed-python)**: Core HED tools for validation, schema management, and analysis
- **[hed-schemas](https://github.com/hed-standard/hed-schemas)**: Official HED schemas in multiple formats
- **[hed-specification](https://github.com/hed-standard/hed-specification)**: Formal HED specification
- **[HED resources](https://www.hed-resources.org)**: User documentation and tutorials
- **[HED online tools](https://hedtools.org)**: Web-based HED tools

## Finding help

### Documentation

- See this documentation for detailed usage guides and API reference
- Visit [HED resources](https://www.hed-resources.org) for general HED documentation
- Check the [hedtools documentation](https://hed-python.readthedocs.io/) for core HED functionality

### Issues and problems

If you encounter bugs or have feature requests:

- **hedvis issues**: [open an issue](https://github.com/hed-standard/hed-vis/issues) in the hed-vis repository
- **hedtools issues**: [open an issue](https://github.com/hed-standard/hed-python/issues) in the hed-python repository

For questions about HED in general, visit the [HED forum](https://github.com/hed-standard/hed-specification/discussions).
