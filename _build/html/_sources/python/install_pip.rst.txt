.. _install-pip:

Installing and Configuring pip
==============================

Follow this guide to install and configure `pip` step by step on your system.

1. Verify pip Installation
--------------------------
   - `pip` is usually installed with Python. To check if it's already installed, run:

     .. code-block:: bash

        pip --version

   - If `pip` is installed, you will see output similar to `pip 23.1.2 from ...`.

2. Install pip (if not already installed)
-----------------------------------------
   - If `pip` is not installed, you can use the following command to install it:
     - For Python 3.x:

       .. code-block:: bash

          python -m ensurepip --upgrade

     - On macOS/Linux, you might need to use `python3`:

       .. code-block:: bash

          python3 -m ensurepip --upgrade

3. Upgrade pip (Recommended)
----------------------------
   - It is always a good practice to keep `pip` updated. Run the following command to upgrade it to the latest version:

     .. code-block:: bash

        pip install --upgrade pip

   - Verify the update by running:

     .. code-block:: bash

        pip --version

4. Install Python Packages with pip
-----------------------------------
   - Now that `pip` is installed and updated, you can use it to install Python packages. For example, to install the `requests` library, run:

     .. code-block:: bash

        pip install requests

   - To verify the installation of a package, you can list installed packages:

     .. code-block:: bash

        pip list

5. Uninstall Python Packages with pip
--------------------------------------
   - To uninstall a package, use the `uninstall` command. For example, to uninstall the `requests` library, run:

     .. code-block:: bash

        pip uninstall requests

6. Install pip for a Specific Python Version (if needed)
--------------------------------------------------------
   - If you have multiple versions of Python installed, specify the version explicitly when running pip commands. For example:
     - For Python 3.x:

       .. code-block:: bash

          python3 -m pip install requests

     - For Python 3.11:

       .. code-block:: bash

          python3.11 -m pip install requests

7. Configure a Virtual Environment (Optional)
---------------------------------------------
   - It's recommended to use a virtual environment for managing dependencies in isolated projects. To set up a virtual environment, use:

     .. code-block:: bash

        python -m venv myenv

   - Activate the virtual environment:
     - On Windows:

       .. code-block:: bash

          myenv\Scripts\activate

     - On macOS/Linux:

       .. code-block:: bash

          source myenv/bin/activate

   - After activation, you can use `pip` to install packages specific to your project.

8. Troubleshooting pip Issues
-----------------------------
   - If you encounter issues with `pip`, you can try reinstalling it. Use the following command:

     .. code-block:: bash

        python -m ensurepip --upgrade --default-pip

   - You can also clear pip’s cache to resolve potential installation issues:

     .. code-block:: bash

        pip cache purge

You now have `pip` installed, upgraded, and configured for managing Python packages.
