.. _install-sphinx:

Installing and Configuring Sphinx
=================================

Follow this guide to install and configure Sphinx step by step on your system.

1. Verify pip Installation
--------------------------
   - Before installing Sphinx, ensure that `pip` is installed and up to date. Run the following command to check:

     .. code-block:: bash

        pip --version

   - If `pip` is not installed, refer to the guide on installing pip.

2. Install Sphinx
-----------------
   - Install Sphinx using `pip`. Run the following command:

     .. code-block:: bash

        pip install sphinx

   - To verify the installation, run:

     .. code-block:: bash

        sphinx-build --version

   - You should see output similar to `sphinx-build 7.x.x`.

3. Set Up a Sphinx Project
--------------------------
   - Navigate to the directory where you want to create your documentation and run:

     .. code-block:: bash

        sphinx-quickstart

   - Follow the prompts to configure your project:
     - Project name
     - Author name
     - Language
     - Enable autodoc and other extensions if needed

4. Install Additional Sphinx Extensions (Optional)
--------------------------------------------------
   - Sphinx has various extensions to enhance its functionality. To install an extension, use `pip`. For example:

     .. code-block:: bash

        pip install sphinx_rtd_theme

   - Add the installed extension to the `extensions` list in your `conf.py` file. For example:

     .. code-block:: python

        extensions = [
            "sphinx_rtd_theme",
        ]

5. Build Your Documentation
---------------------------
   - To generate the documentation, navigate to your project directory and run:

     .. code-block:: bash

        make html

   - The generated HTML files will be available in the `_build/html` directory.

6. Preview Your Documentation
-----------------------------
   - Open the generated HTML files in your web browser. For example, to open the main page, run:

     .. code-block:: bash

        open _build/html/index.html

   - On Windows, use:

     .. code-block:: bash

        start _build/html/index.html

7. Customize Your Documentation
-------------------------------
   - Edit the `.rst` files in your project directory to update content and structure.
   - Update the `conf.py` file to configure project settings like theme, extensions, and metadata.

8. Rebuild Your Documentation After Changes
-------------------------------------------
   - Each time you modify your `.rst` files or `conf.py`, rebuild the documentation by running:

     .. code-block:: bash

        make html

   - Refresh your browser to see the updated documentation.

9. Troubleshooting Sphinx Issues
---------------------------------
   - If you encounter issues, ensure that Sphinx and its extensions are up to date:

     .. code-block:: bash

        pip install --upgrade sphinx

   - Clear the build directory and rebuild the documentation if needed:

     .. code-block:: bash

        make clean
        make html

10. Install Sphinx in a Virtual Environment (Optional)
------------------------------------------------------
   - To avoid conflicts with other Python projects, set up a virtual environment:

     .. code-block:: bash

        python -m venv sphinx_env

   - Activate the virtual environment:
     - On Windows:

       .. code-block:: bash

          sphinx_env\Scripts\activate

     - On macOS/Linux:

       .. code-block:: bash

          source sphinx_env/bin/activate

   - Install Sphinx in the virtual environment:

     .. code-block:: bash

        pip install sphinx

You now have Sphinx installed, configured, and ready for creating professional documentation.
