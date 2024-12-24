Customizing Fonts and Colors
=============================

Step 1: Create a `custom.css` File
----------------------------------
1. Navigate to your `_static` folder (or create it in your project directory if it doesn't exist).
2. Inside the `_static` folder, create a file named `custom.css`.

Example:

.. code-block:: css

   /* Change font family */
   body {
       font-family: 'Arial', sans-serif; /* Replace with your desired font */
   }

   /* Change navigation bar background color */
   .wy-side-nav-search {
       background-color: #2c3e50; /* Replace with your desired color */
   }

   /* Change navigation link color */
   .wy-nav-side a {
       color: #1abc9c; /* Replace with your desired color */
   }

   /* Change header text color */
   h1, h2, h3, h4, h5, h6 {
       color: #34495e; /* Replace with your desired color */
   }

   /* Customize hover effect on links */
   .wy-nav-side a:hover {
       color: #e74c3c;
   }

Step 2: Link the Custom CSS in `conf.py`
----------------------------------------
1. Open the `conf.py` file in your project directory.
2. Add the following configuration to link the `custom.css` file:

.. code-block:: python

   html_static_path = ["_static"]  # Ensure the _static directory is included
   html_css_files = [
       "custom.css",  # Add your custom CSS file
   ]

Step 3: Test the Customizations
-------------------------------
1. Run the following command to rebuild your documentation:

.. code-block:: bash

   make html

2. Open the generated HTML files from the `_build/html` directory in your browser.
3. Verify that the custom fonts and colors have been applied.

Step 4: Experiment with Additional Styling
------------------------------------------
1. Use developer tools in your browser to inspect elements and experiment with styles.
2. Update the `custom.css` file as needed to fine-tune the appearance of your documentation.

Step 5: Use Google Fonts (Optional)
-----------------------------------
1. Go to [Google Fonts](https://fonts.google.com/) and select your desired font.
2. Add the following `@import` rule to the top of your `custom.css` file:

.. code-block:: css

   @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

3. Update the `body` font-family in your CSS:

.. code-block:: css

   body {
       font-family: 'Roboto', sans-serif;
   }

Step 6: Customize Theme Options in `conf.py` (Optional)
--------------------------------------------------------
1. Open `conf.py` and configure additional theme options for colors if supported by your theme.
2. For `sphinx_rtd_theme`, add options like this:

.. code-block:: python

   html_theme_options = {
       "style_nav_header_background": "#34495e",  # Change navigation header color
   }

Step 7: Rebuild and Review
--------------------------
1. Run `make html` to rebuild your site with the updated styles.
2. Check the output to confirm that all changes are reflected.

Congratulations! You have successfully customized fonts and colors in your Sphinx documentation.
