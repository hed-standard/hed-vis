# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2026-01-28

### Minor cosmetic changes

- Corrected the `README.md` file and updated the badges.
- Removed unused dependencies
- Added explicit requirement pandas\<3.0.0.

## [0.1.0] - 2026-01-26

### Added

#### Core features

- **HedTagVisualizer API**: Modern configuration-based interface for generating visualizations from HED-annotated data

  - Support for creating word clouds from HED tag frequency data
  - Integration with hedtools data structures (HedTagCounts, TabularInput, HedString)
  - Flexible configuration system using VisualizationConfig and WordCloudConfig classes
  - Multiple output format support (PNG and SVG)
  - Direct processing from tabular data or pre-computed tag counts
  - Tag template support for organizing tags by categories
  - Context-aware tag processing with options for including context and replacing definitions

- **Legacy word cloud API**: Simple functional interface for quick word cloud generation

  - `create_wordcloud()`: Create word clouds from frequency dictionaries
  - `word_cloud_to_svg()`: Export word clouds to SVG format
  - Backward compatibility support for users familiar with simpler APIs

- **Word cloud customization**:

  - Configurable dimensions (width and height)
  - Custom background colors with transparency support
  - Mask image support for shaped word clouds (with built-in brain mask)
  - Customizable color schemes via colormaps
  - Advanced layout options (horizontal preference, font sizes, contours)
  - Font customization with validation
  - Smart automatic sizing with minimum size constraints

- **Sequence map utility**: Class for mapping between event sequences and display text

  - Convert between compact and verbose event representations
  - Tag template-based categorization
  - Count tracking for frequency analysis

#### Command-line tools

- **visualize_hed_tags.py**: Comprehensive CLI script for batch processing
  - Process entire directory trees of HED-annotated TSV files
  - Automatic discovery and pairing of event files with JSON sidecars
  - File filtering by prefix, suffix, and custom patterns
  - Directory exclusion for focused processing
  - HED schema version selection (automatic or manual)
  - Tag template support via JSON files
  - Multiple output options (word cloud, tag counts JSON, summaries)
  - Configurable logging with multiple verbosity levels
  - Progress tracking for large datasets
  - Support for BIDS-style dataset organization

#### Testing infrastructure

- Comprehensive test suite with 100+ test cases
  - `test_tag_visualizer.py`: Tests for HedTagVisualizer class and core visualization logic
  - `test_tag_word_cloud.py`: Tests for legacy word cloud API
  - `test_visualization_config.py`: Tests for configuration classes and validation
  - `test_sequence_map.py`: Tests for sequence mapping utilities
- Test data including real HED-annotated event files
- Integration tests with actual hedtools components
- Configuration validation tests
- Output format verification tests

#### Documentation

- **Complete Sphinx documentation**:

  - Overview and introduction to hedvis
  - Comprehensive user guide with multiple examples
  - Detailed API reference for all public classes and functions
  - Integration guides for hedtools workflows
  - Custom CSS styling and branding
  - Read the Docs integration

- **README.md**: Quick start guide with examples

  - Installation instructions
  - Feature highlights
  - Usage examples for both new and legacy APIs
  - Integration examples with hedtools
  - Links to documentation and related projects

- **CONTRIBUTING.md**: Contribution guidelines

  - Development setup instructions
  - Coding standards and best practices
  - Testing guidelines
  - Pull request process
  - Code quality requirements

- **RELEASE_GUIDE.md**: Detailed release procedures

  - Step-by-step release checklist
  - PyPI publishing instructions
  - Version management guidelines
  - Pre-release validation steps

#### Examples

- `quick_demo.py`: Demonstration script showing:
  - Dictionary-based configuration
  - Object-oriented configuration with config classes
  - Legacy API usage
  - SVG generation

#### Development infrastructure

- **Package configuration**:

  - Modern pyproject.toml-based packaging
  - Support for Python 3.10 through 3.14
  - Comprehensive dependency management
  - Entry point for command-line script
  - Development dependencies specification
  - Black code formatter configuration
  - Ruff linter configuration

- **Continuous integration**:

  - Multi-platform testing (Linux, Windows, macOS)
  - Python version matrix testing (3.10, 3.11, 3.12, 3.13, 3.14)
  - Code coverage reporting with codecov
  - Automated code quality checks:
    - Black code formatter validation
    - Ruff linting
    - Codespell for spelling errors
    - Link checker for documentation
    - Markdown formatting validation
  - Documentation building and deployment
  - Test installer verification
  - Dependabot for automated dependency updates

- **Code quality tools**:

  - Black formatter configuration
  - Ruff linter with custom rules
  - Codespell with custom dictionary
  - Pre-commit hook support
  - Coverage configuration with exclusions

- **Git configuration**:

  - Comprehensive .gitignore for Python projects
  - .gitattributes for consistent line endings
  - Git submodules configuration

#### Resources

- Built-in brain mask image for shaped word clouds
- Default color schemes optimized for tag visualization

### Dependencies

- hedtools >= 0.8.1 for HED processing
- wordcloud for word cloud generation
- matplotlib >= 3.9.0 for visualization
- Pillow for image processing
- numpy for numerical operations
- pandas for data handling
- Additional utility dependencies (click, jsonschema, inflect, etc.)

### Infrastructure

- MIT License
- GitHub Actions CI/CD pipeline
- PyPI package distribution
- Read the Docs documentation hosting
- Code coverage tracking
- Automated dependency updates

______________________________________________________________________

**Note**: This is the initial public release of hedvis. The package provides visualization tools specifically designed for HED (Hierarchical Event Descriptors) annotated datasets, with a focus on word cloud generation and visual summaries. It integrates seamlessly with the hedtools ecosystem while providing both modern and legacy APIs for flexibility.
