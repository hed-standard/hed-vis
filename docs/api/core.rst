Core API
========

Main visualization interface
-----------------------------

.. automodule:: hedvis.core.tag_visualizer
   :members:
   :undoc-members:
   :show-inheritance:

HedTagVisualizer
~~~~~~~~~~~~~~~~

.. autoclass:: hedvis.core.tag_visualizer.HedTagVisualizer
   :members:
   :undoc-members:
   :show-inheritance:

   The main class for generating HED tag visualizations.

   **Key Methods:**

   * :meth:`visualize_from_counts` - Generate visualizations from pre-computed tag counts
   * :meth:`visualize_from_tabular` - Generate visualizations from tabular data
   * :meth:`visualize_from_dataframe` - Generate visualizations from pandas DataFrame

   **Examples:**

   Basic usage with tag counts::

       from hedvis import HedTagVisualizer
       
       visualizer = HedTagVisualizer()
       results = visualizer.visualize_from_counts(tag_counts)
       results['word_cloud']['wordcloud_object'].to_file('output.png')

   With custom configuration::

       from hedvis import HedTagVisualizer, WordCloudConfig, VisualizationConfig
       
       wc_config = WordCloudConfig(width=1200, height=800)
       viz_config = VisualizationConfig(word_cloud=wc_config)
       visualizer = HedTagVisualizer(viz_config)

Sequence map
------------

.. automodule:: hedvis.core.sequence_map
   :members:
   :undoc-members:
   :show-inheritance:
