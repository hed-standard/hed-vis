"""Visualization tools for HED."""

__version__ = "0.1.0"

# New API - recommended for all new code
from .core import HedTagVisualizer, VisualizationConfig, WordCloudConfig

# Legacy API - for backward compatibility
from .generators.word_cloud import create_wordcloud, word_cloud_to_svg

__all__ = [
    # New API
    "HedTagVisualizer",
    "VisualizationConfig",
    "WordCloudConfig",
    # Legacy API
    "create_wordcloud",
    "word_cloud_to_svg",
]
