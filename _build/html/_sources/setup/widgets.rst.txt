Adding Widgets and Logo
=======================

This guide explains how to add **attention** and **note** widgets to your `.rst` files, complete with both the code and the rendered output.

Attention Widget
-----------------

**Code Block**

.. code-block:: rst

   .. attention::

      Here be dragons 🐉

      This is the **latest** (unstable) version of this documentation, which may document features not available in or compatible with released stable versions of the software.

      See the `stable version <https://example.com/stable>`_ of this documentation page instead.

**Rendered Widget**

.. attention::

   Here be dragons 🐉

   This is the **latest** (unstable) version of this documentation, which may document features not available in or compatible with released stable versions of the software.

   See the `stable version <https://example.com/stable>`_ of this documentation page instead.

Note Widget
-----------

**Code Block**

.. code-block:: rst

   .. note::

      The documentation is available in various languages and versions. Expand the "Read the Docs" panel at the bottom of the sidebar to see the list.

**Rendered Widget**

.. note::

   The documentation is available in various languages and versions. Expand the "Read the Docs" panel at the bottom of the sidebar to see the list.

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

Add Images
----------

1. **Create the `_static` Directory**
   Ensure your project has a `_static` folder in its root directory. If it doesn’t exist, create it manually. This is where all your static files, including images, will be stored.

   Example structure:

   .. code-block:: text

      your_project/
      ├── _static/
      ├── _templates/
      ├── conf.py
      ├── index.rst
      ├── page1.rst

2. **Organize Images in `_static/images`**
   Inside `_static`, create an `images` folder. Place your image files here to keep them organized.

   Example structure:

   .. code-block:: text

      your_project/
      ├── _static/
      │   └── images/
      │       ├── example.png
      │       ├── diagram.jpg
      │       └── logo.svg
      ├── conf.py
      ├── index.rst

3. **Reference Images in `.rst` Files**
   Use the `.. image::` directive to add images. Paths must be relative to the root directory.

   Basic syntax:

   .. code-block:: rst

      .. image:: _static/images/example.png
         :alt: Example Image
         :width: 50%

   - `:alt:` Adds alternative text for accessibility.
   - `:width:` Adjusts the image width (e.g., `300px` or `50%`).

4. **Adding Captions with `.. figure::`**
   For captions, use the `.. figure::` directive instead of `.. image::`.

   Example:

   .. code-block:: rst

      .. figure:: _static/images/diagram.jpg
         :alt: System Diagram
         :width: 300px

         This diagram illustrates the architecture of our system.

5. **Update the `conf.py` File**
   Ensure `_static` is properly configured by setting the `html_static_path` in `conf.py`:

   .. code-block:: python

      html_static_path = ['_static']

6. **Build Your Documentation**
   Rebuild your documentation after making changes:

   .. code-block:: bash

      make html

   This will generate the updated HTML in the `_build/html` folder.

7. **Troubleshooting**
   - If an image doesn’t display:

     - Ensure the file path is correct and matches the location in `_static/images`.
     - Verify that the file name and path are case-sensitive.
     - Confirm that `html_static_path` is set in `conf.py`.

   - For build errors:
   
     - Check for typos in file paths or names.
     - Confirm the `_static` folder exists and contains your images.

**Congratulations!** You now know how to add and manage images in Sphinx documentation with precision and clarity.

