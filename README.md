# hed-vis

[![Documentation Status](https://readthedocs.org/projects/hed-vis/badge/?version=latest)](https://hed-vis.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/hedvis.svg)](https://badge.fury.io/py/hedvis)
[![Python](https://img.shields.io/pypi/pyversions/hedvis.svg)](https://pypi.org/project/hedvis/)

Visualization tools for HED (Hierarchical Event Descriptors) annotated datasets.

**hedvis** provides word cloud generation and visual summaries for HED-annotated data, making it easy to explore and present the semantic content of your experimental datasets.

## Features

- **Word Cloud Generation** - Create beautiful word clouds from HED tag frequencies
- **Flexible Configuration** - Extensive customization options for visualizations
- **Shaped Clouds** - Support for mask images to create custom-shaped word clouds
- **Multiple Formats** - Export to PNG and SVG formats
- **hedtools Integration** - Seamless integration with the HED Python tools ecosystem
- **Two APIs** - Modern configuration-based API and simple legacy API for quick tasks

## Installation

Install from PyPI:

```bash
pip install hedvis
```

This automatically installs hedtools and other required dependencies.

For development installation:

```bash
git clone https://github.com/hed-standard/hed-vis.git
cd hed-vis
pip install -e .
```

## Quick Start

### Simple Word Cloud

```python
from hedvis import create_wordcloud

# Create word cloud from frequency dictionary
word_freq = {
    "Event": 15,
    "Action": 10,
    "Sensory-event": 8,
    "Visual-presentation": 7
}

wc = create_wordcloud(word_freq, width=800, height=600)
wc.to_file("wordcloud.png")
```

### Using the New API

```python
from hedvis import HedTagVisualizer, WordCloudConfig, VisualizationConfig

# Configure visualization
wc_config = WordCloudConfig(
    width=1200,
    height=800,
    background_color="white",
    colormap="viridis"
)

viz_config = VisualizationConfig(
    word_cloud=wc_config,
    output_formats=["png", "svg"]
)

# Create visualizer
visualizer = HedTagVisualizer(viz_config)

# Generate from HED tag counts (from hedtools)
results = visualizer.visualize_from_counts(tag_counts)
```

### Integration with hedtools

```python
from hed import load_schema
from hed.models import TabularInput
from hedvis import HedTagVisualizer

# Load HED schema and data
schema = load_schema()
tabular = TabularInput("events.tsv", sidecar="events.json")

# Create visualizer
visualizer = HedTagVisualizer()

# Generate visualizations
results = visualizer.visualize_from_tabular(
    tabular,
    schema,
    output_basename="experiment_tags"
)

# Save word cloud
results['word_cloud']['wordcloud_object'].to_file("tags.png")
```

## Documentation

Full documentation is available at [Read the Docs](https://hed-vis.readthedocs.io/):

- [Introduction](https://hed-vis.readthedocs.io/en/latest/introduction.html)
- [User Guide](https://hed-vis.readthedocs.io/en/latest/user_guide.html)
- [API Reference](https://hed-vis.readthedocs.io/en/latest/api/index.html)

## Requirements

- Python 3.10+
- hedtools
- wordcloud
- matplotlib
- Pillow
- numpy

## Related Projects

- **[hedtools](https://github.com/hed-standard/hed-python)** - Core HED tools for validation and analysis
- **[hed-schemas](https://github.com/hed-standard/hed-schemas)** - Official HED schemas
- **[hed-specification](https://github.com/hed-standard/hed-specification)** - HED specification
- **[HED Resources](https://www.hed-resources.org)** - User documentation and tutorials

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Issues

For bug reports and feature requests, please [open an issue](https://github.com/hed-standard/hed-vis/issues) on GitHub.

For general HED questions, visit the [HED forum](https://github.com/hed-standard/hed-specification/discussions).

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Citation

If you use hedvis in your research, please cite:

```
HED Visualization Tools (hedvis)
https://github.com/hed-standard/hed-vis
```

For HED in general, please cite the HED specification paper.
