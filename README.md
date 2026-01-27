![PyPI - Status](https://img.shields.io/pypi/v/hedvis) ![Python3](https://img.shields.io/badge/python-%3E=3.10-yellow.svg) [![Docs](https://img.shields.io/badge/docs-hedvis-blue.svg)](https://www.hedtags.org/hed-vis)

# HED visualization hed

Visualization tools for `HED (Hierarchical Event Descriptors)` annotated datasets.

**hedvis** provides `word cloud` generation and `visual summaries <visualization>` for `HED-annotated data <dataset; HED-annotated>`, making it easy to explore and present the semantic content of your experimental datasets.

## Features

- **Word Cloud Generation** - Create beautiful word clouds from `HED tag frequencies <tag frequency>`
- **Flexible Configuration** - Extensive `customization <configuration>` options for visualizations
- **Shaped Clouds** - Support for `mask images <mask image>` to create custom-shaped word clouds
- **Multiple Formats** - Export to `PNG <PNG format>` and `SVG <SVG format>` formats
- **hedtools Integration** - Seamless integration with the `HED Python tools <hedtools>` ecosystem
- **Two APIs** - Modern `configuration-based API <VisualizationConfig>` and simple `legacy API <API; legacy>` for quick tasks

## Installation

### From PyPI (Recommended)

Install the latest stable release:

```bash
pip install hedvis
```

This automatically installs hedtools and all required dependencies.

### Development Installation

For development work, clone the repository and install in editable mode:

```bash
git clone https://github.com/hed-standard/hed-vis.git
cd hed-vis
pip install -e .
```

### Installing Optional Dependencies

**The project uses `pyproject.toml` as the single source of truth for all dependencies.** Install optional dependencies using pip extras.

**Important:** Installing with extras automatically includes all base dependencies (hedtools, numpy, pandas, etc.) plus the extra tools.

**Development tools** (code formatting, linting, testing):

```bash
# From PyPI (if you installed hedvis from PyPI)
pip install "hedvis[dev]"

# From local source (if you cloned the repository)
pip install ".[dev]"          # Regular install
pip install -e ".[dev]"       # Editable install (recommended for development)
```

**Documentation tools** (Sphinx, themes):

```bash
# From PyPI
pip install "hedvis[docs]"

# From local source
pip install ".[docs]"
```

**Both dev and docs dependencies**:

```bash
# From PyPI
pip install "hedvis[dev,docs]"

# From local source
pip install ".[dev,docs]"
```

### Installing from Source Without Extras

To install from source with only the core dependencies:

```bash
git clone https://github.com/hed-standard/hed-vis.git
cd hed-vis
pip install .
```

### Legacy Requirements Files

**Important:** Legacy requirements files (`requirements.txt`, `requirements-dev.txt`, `docs/requirements.txt`) are deprecated and should not be used. All dependencies are now managed in `pyproject.toml`, which is the canonical source. These files will be removed in a future release.

If you need to install dependencies for development or documentation:

- Use `pip install ".[dev]"` instead of `pip install -r requirements-dev.txt`
- Use `pip install ".[docs]"` instead of `pip install -r docs/requirements.txt`
- Core dependencies are installed automatically with `pip install .` or `pip install hedvis`

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
- hedtools (>=0.8.1)
- wordcloud (>=1.9.4)
- matplotlib (>=3.9.0)
- Pillow (>=11.2.1)
- numpy (>=2.0.2)
- pandas (>=2.2.3)

All dependencies are managed in `pyproject.toml` and installed automatically with `pip install hedvis`.

For the complete list of dependencies with exact versions, see the `dependencies` section in [pyproject.toml](pyproject.toml).

## Related Projects

- **[hedtools](https://github.com/hed-standard/hed-python)** - Core HED tools for validation and analysis
- **[hed-schemas](https://github.com/hed-standard/hed-schemas)** - Official HED schemas
- **[hed-specification](https://github.com/hed-standard/hed-specification)** - HED specification
- **[HED Resources](https://www.hed-resources.org)** - User documentation and tutorials

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Support

- [Documentation](https://www.hedtags.org/hed-vis)
- [GitHub issues](https://github.com/hed-standard/hed-vis/issues)
- [Ideas or questions](https://github.com/orgs/hed-standard/discussions)
- [HED Homepage](https://www.hedtags.org)
- Contact: [hed-maintainers@gmail.com](mailto:hed-maintainers@gmail.com)

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Citation

If you use hedvis in your research, please cite:

If you use HEDTools in your research, please cite:

```bibtex
@software{hedtools,
  author = {Ian Callanan, Robbins, Kay and others},
  title = {HEDVis: Visualization tools for HED},
  year = {2024},
  publisher = {GitHub},
  url = {https://github.com/hed-standard/hed-vis},
}
```
