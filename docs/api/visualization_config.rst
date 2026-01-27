hedvis configuration classes
============================

Visualization configuration
---------------------------

.. automodule:: hedvis.core.visualization_config
   :undoc-members:
   :show-inheritance:

VisualizationConfig
~~~~~~~~~~~~~~~~~~~

.. autoclass:: hedvis.core.visualization_config.VisualizationConfig
   :members:
   :show-inheritance:

   Main configuration class for visualization generation.

   **Attributes:**

   * **word_cloud** (*WordCloudConfig*) - Word cloud settings
   * **output_formats** (*list*) - List of output formats ['png', 'svg']
   * **save_directory** (*str*) - Directory for saving outputs
   * **save_files** (*bool*) - Whether to automatically save files

   **Example:**

   ::

       from hedvis import VisualizationConfig, WordCloudConfig
       
       config = VisualizationConfig(
           word_cloud=WordCloudConfig(width=1000, height=600),
           output_formats=["png", "svg"],
           save_directory="./outputs",
           save_files=True
       )

   From dictionary::

       config_dict = {
           "word_cloud": {"width": 800, "height": 600},
           "output_formats": ["svg"]
       }
       config = VisualizationConfig.from_dict(config_dict)

WordCloudConfig
~~~~~~~~~~~~~~~

.. autoclass:: hedvis.core.visualization_config.WordCloudConfig
   :members:
   :show-inheritance:

   Configuration for word cloud visualizations.

   **Dimension Attributes:**

   * **width** (*int*) - Width in pixels (default: 800)
   * **height** (*int*) - Height in pixels (default: 600)

   **Appearance Attributes:**

   * **background_color** (*str or None*) - Background color (None for transparent)
   * **prefer_horizontal** (*float*) - Fraction of horizontal text (0.0-1.0)
   * **min_font_size** (*int*) - Minimum font size
   * **max_font_size** (*int or None*) - Maximum font size (auto if None)

   **Font Attributes:**

   * **font_path** (*str or None*) - Path to custom font file (.ttf, .otf)

   **Color Scheme Attributes:**

   * **colormap** (*str*) - Matplotlib colormap name (default: 'nipy_spectral')
   * **color_range** (*tuple*) - (min, max) range of colormap to use
   * **color_step_range** (*tuple*) - (min, max) step sizes through colormap

   **Mask Attributes:**

   * **use_mask** (*bool*) - Whether to use mask image
   * **mask_path** (*str or None*) - Path to mask image
   * **contour_width** (*int*) - Width of contour line
   * **contour_color** (*str*) - Color of contour line

   **Scaling Attributes:**

   * **scale_adjustment** (*float*) - Frequency scaling adjustment
   * **relative_scaling** (*float*) - Word size scaling factor (0.0-1.0)

   **Example:**

   Basic configuration::

       from hedvis import WordCloudConfig
       
       config = WordCloudConfig(
           width=1200,
           height=800,
           background_color="white",
           colormap="viridis"
       )

   Masked word cloud::

       config = WordCloudConfig(
           use_mask=True,
           mask_path="brain_outline.png",
           background_color="white",
           contour_width=3,
           contour_color="navy"
       )

   Custom colors and fonts::

       config = WordCloudConfig(
           font_path="/path/to/custom-font.ttf",
           colormap="plasma",
           color_range=(0.2, 0.8),
           prefer_horizontal=0.9
       )
