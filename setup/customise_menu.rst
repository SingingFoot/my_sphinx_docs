Creating and Customizing the Menu
==================================

Step 1: Create the Folder Structure
------------------------------------
1. Organize your content into logical folders (e.g., `python`, `setup`, `sphinx`).
2. Each folder should contain related `.rst` files (e.g., `install_python.rst` in the `python` folder).

Step 2: Configure the Main Index File (`index.rst`)
---------------------------------------------------
1. Open your `index.rst` file.
2. Use `toctree` directives to create collapsible menus for each section.

Example:

.. code-block:: rst

   .. toctree::
      :hidden:
      :caption: Python and PIP
      :maxdepth: 1

      python/install_python
      python/install_pip

   .. toctree::
      :hidden:
      :caption: Sphinx and Read the Docs
      :maxdepth: 1

      sphinx/install_sphinx
      sphinx/install_readthedocs

   .. toctree::
      :hidden:
      :caption: Set Up Your Website
      :maxdepth: 1

      setup/customise_menu
      setup/customise_colors
      setup/widgets

Step 3: Create Each `.rst` File
-------------------------------
1. Inside each folder, create `.rst` files for every topic.
2. Each `.rst` file should contain content relevant to its topic.

Example (`install_python.rst`):

.. code-block:: rst

   Installing Python
   =================

   Step 1: Download Python from the official website.
   --------------------------------------------------
   Visit https://www.python.org/downloads/ and choose the appropriate version.

   Step 2: Install Python on your system.
   --------------------------------------
   Follow the installer instructions to complete the setup.

Step 4: Update `conf.py` to Support Customization
-------------------------------------------------
1. Ensure the following is included in your `conf.py` file:

.. code-block:: python

   html_theme = "sphinx_rtd_theme"
   html_theme_options = {
       "collapse_navigation": True,  # Enables collapsible menus
       "navigation_depth": 2,       # Limits how deep the menus expand
   }

Step 5: Build the Documentation
-------------------------------
1. Run the following command to build your website:

.. code-block:: bash

   make html

2. Check the `_build/html` folder for the output.

Step 6: Review and Adjust
-------------------------
1. Open the generated documentation in your browser.
2. Review the menu structure and ensure collapsibility works as expected.

Step 7: Customize the Menu Styling (Optional)
---------------------------------------------
1. Add a `custom.css` file to the `_static` folder for additional style changes.
2. Link the CSS in `conf.py`:

.. code-block:: python

   html_css_files = [
       "custom.css",
   ]

That's it! This structure will give you a clean and collapsible menu like the one you desire.
