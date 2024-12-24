Widgets
=======

.. _add-logo-guide:

Adding a Logo with Alpha Channel and Hyperlink
----------------------------------------------

This guide provides step-by-step instructions to add a logo with an alpha channel and link it to the main page of your Sphinx documentation.


1. **Prepare Your Logo File**
   - Create or edit your logo with a transparent background (alpha channel).
   - Resize it to an appropriate size (e.g., 100x100 pixels) to fit in the sidebar.
   - Save the logo as a `.png` file, e.g., `my_logo.png`.

2. **Place the Logo in the `_static` Directory**
   - Copy your `my_logo.png` file into the `_static` directory of your Sphinx project.

   Example:

   .. code-block:: bash

      cp my_logo.png _static/

3. **Add a Custom CSS File**
   - Create a file named `custom.css` in the `_static` directory.
   - Add the following CSS code to control the logo size and position:

   .. code-block:: css

      /* Adjust the logo size in the sidebar */
      .wy-side-nav-search img {
          max-width: 100px; /* Adjust width */
          max-height: 100px; /* Adjust height */
          margin: 0 auto;
          display: block;
          border-radius: 8px; /* Optional: rounded corners */
          background-color: transparent; /* Ensure background is clear */
      }

4. **Link the CSS File in `conf.py`**
   - Open your `conf.py` file.
   - Add the following line to include the `custom.css` file:

   .. code-block:: python

      html_css_files = [
          "custom.css",
      ]

5. **Add the Logo and Hyperlink**
   - In your `conf.py` file, add the following code to specify the logo and link it to the main page:

   .. code-block:: python

      html_logo = "_static/my_logo.png"

      # Add a hyperlink to the logo
      html_theme_options = {
          "logo_url": "/",  # Links the logo to the root of your site
      }

6. **Rebuild Your Documentation**
   - Run the following command to rebuild your documentation and apply the changes:

   .. code-block:: bash

      make html

7. **Verify the Logo**
   - Open the generated `index.html` file in the `_build/html` directory in your browser.
   - Check if the logo is displayed with the correct size, transparency, and a hyperlink to the main page.

That's it! Your logo should now appear on your Sphinx website with an alpha channel and a clickable link to the main page.
