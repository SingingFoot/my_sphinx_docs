==============================
Install Read the Docs Theme
==============================

This guide will walk you through the steps required to install and configure the Read the Docs Theme for your Sphinx documentation project.

Step 1: Ensure Sphinx is Installed
----------------------------------
Before you can install the Read the Docs Theme, make sure you have Sphinx installed. If you don't, follow the guide on how to install Sphinx.

Run the following command to check:

.. code-block:: bash

    sphinx-build --version

If it's not installed, install it using:

.. code-block:: bash

    pip install sphinx

Step 2: Install the Theme
-------------------------
Install the Read the Docs Theme using pip:

.. code-block:: bash

    pip install sphinx_rtd_theme

This command will download and install the theme and make it available for use in your Sphinx project.

Step 3: Edit `conf.py`
----------------------
Open your `conf.py` file in the root of your Sphinx documentation directory. Update the following configuration:

1. Set the `html_theme` option to `"sphinx_rtd_theme"`:

   .. code-block:: python

       html_theme = "sphinx_rtd_theme"

2. (Optional) Customize the theme by adding `html_theme_options`:

   .. code-block:: python

       html_theme_options = {
           "collapse_navigation": True,
           "navigation_depth": 4,
       }

   These options control how the theme behaves. For example:
   - **collapse_navigation**: Collapses the navigation menu by default.
   - **navigation_depth**: Limits the depth of the navigation tree.

Step 4: Build Your Documentation
--------------------------------
After making changes to `conf.py`, rebuild your documentation to apply the new theme:

.. code-block:: bash

    make html

The output will be generated in the `_build/html` directory. Open the `index.html` file in your browser to see the theme in action.

Step 5: Verify Installation
---------------------------
Open the generated documentation in your browser to confirm that the Read the Docs Theme is applied correctly.

Step 6: Additional Customizations
---------------------------------
You can further customize the theme by adding CSS or overriding templates. For example:

1. Create a `_static/` directory if it doesn't already exist.
2. Add custom styles in `_static/custom.css` and include it in `conf.py`:

   .. code-block:: python

       html_static_path = ["_static"]
       html_css_files = [
           "custom.css",
       ]

3. Rebuild your documentation to apply custom styles.

That's it! You now have the Read the Docs Theme installed and ready to use for your documentation project.
