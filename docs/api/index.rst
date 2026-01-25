API reference
=============

This section contains the complete API reference for HED Visualization Tools (hedvis).

.. toctree::
   :maxdepth: 2

   core
   generators
   visualization_config

Core modules overview
---------------------

The hedvis package is organized into several key modules:

* **Core**: Main visualization API with `HedTagVisualizer` class
* **Generators**: Word cloud generation functions and utilities
* **Configuration**: Configuration classes for customizing visualizations

Quick API reference
-------------------

New API (Recommended)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from hedvis import HedTagVisualizer, VisualizationConfig, WordCloudConfig

   # Create visualizer with configuration
   config = WordCloudConfig(width=800, height=600)
   visualizer = HedTagVisualizer(VisualizationConfig(word_cloud=config))

   # Generate visualizations from tag counts
   results = visualizer.visualize_from_counts(tag_counts)

Legacy API
~~~~~~~~~~

.. code-block:: python

   from hedvis import create_wordcloud, word_cloud_to_svg

   # Create word cloud from dictionary
   wc = create_wordcloud(word_freq, width=800, height=600)
   wc.to_file("output.png")

   # Convert to SVG
   svg = word_cloud_to_svg(wc)
