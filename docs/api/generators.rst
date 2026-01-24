Word cloud generators
====================

Word cloud creation
-------------------

.. automodule:: hedvis.generators.word_cloud
   :members:
   :undoc-members:
   :show-inheritance:

create_wordcloud
~~~~~~~~~~~~~~~~

.. autofunction:: hedvis.generators.word_cloud.create_wordcloud

   Create a word cloud from a dictionary of word frequencies.

   **Parameters:**

   * **word_dict** (*dict*) - Dictionary mapping words to their frequencies
   * **mask_path** (*str or None*) - Path to mask image for shaped clouds
   * **background_color** (*str or None*) - Background color (None for transparent)
   * **width** (*int*) - Width in pixels (default: 400)
   * **height** (*int*) - Height in pixels (default: 300)
   * **kwargs** - Additional parameters passed to WordCloud

   **Returns:**

   * **WordCloud** - Generated word cloud object

   **Raises:**

   * **ValueError** - If word_dict is empty
   * **HedFileError** - If font or mask path is invalid

   **Examples:**

   Basic word cloud::

       from hedvis import create_wordcloud
       
       word_freq = {"Event": 10, "Action": 5, "Sensory": 8}
       wc = create_wordcloud(word_freq, width=800, height=600)
       wc.to_file("wordcloud.png")

   With mask image::

       wc = create_wordcloud(
           word_freq,
           mask_path="brain_mask.png",
           background_color="white"
       )

word_cloud_to_svg
~~~~~~~~~~~~~~~~~

.. autofunction:: hedvis.generators.word_cloud.word_cloud_to_svg

   Convert a WordCloud object to SVG string format.

   **Parameters:**

   * **wc** (*WordCloud*) - The word cloud object to convert

   **Returns:**

   * **str** - SVG representation as string

   **Example:**

   ::

       from hedvis import create_wordcloud, word_cloud_to_svg
       
       wc = create_wordcloud(word_freq)
       svg_string = word_cloud_to_svg(wc)
       
       with open("output.svg", "w") as f:
           f.write(svg_string)

load_and_resize_mask
~~~~~~~~~~~~~~~~~~~~

.. autofunction:: hedvis.generators.word_cloud.load_and_resize_mask

   Load and resize a mask image for word cloud generation.

   **Parameters:**

   * **mask_path** (*str*) - Path to mask image
   * **width** (*int, optional*) - Target width
   * **height** (*int, optional*) - Target height

   **Returns:**

   * **numpy.ndarray** - Processed mask image as binary array

Word cloud utilities
--------------------

.. automodule:: hedvis.generators.word_cloud_util
   :members:
   :undoc-members:
   :show-inheritance:

   Color Functions
   ~~~~~~~~~~~~~~~

   .. autofunction:: hedvis.generators.word_cloud_util.default_color_func

      Default color function for word clouds using matplotlib colormaps.

   .. autofunction:: hedvis.generators.word_cloud_util.generate_contour_svg

      Generate SVG contour overlay for masked word clouds.
