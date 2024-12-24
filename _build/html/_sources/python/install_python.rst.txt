.. _install-python:

Installing Python
=================

Follow this guide to install Python step by step on your system.

1. Download Python
------------------
   - Visit the official Python website and navigate to the `Downloads section <https://www.python.org/downloads/>`_.
   - Choose the appropriate version for your operating system (e.g., macOS, Windows, or Linux).
   - Click the download link to get the installer.

2. Run the Installer
--------------------
   - Locate the downloaded installer file on your system.
   - Double-click the installer to start the installation process.
   - Follow the on-screen instructions:
     - On Windows, check the box **"Add Python to PATH"** before proceeding.
     - On macOS/Linux, ensure you have the necessary permissions to install software.

3. Verify Installation
----------------------
   - Open your terminal (Command Prompt, PowerShell, or Bash).
   - Run the following command to check the Python version:

     .. code-block:: bash

        python --version

   - Alternatively, use the `python3` command if `python` defaults to an older version:

     .. code-block:: bash

        python3 --version

   - You should see output displaying the installed Python version, e.g., `Python 3.11.3`.

4. Install pip (Optional)
-------------------------
   - Python usually comes with `pip` pre-installed. To verify, run:

     .. code-block:: bash

        pip --version

   - If `pip` is not installed, run the following command to install it:

     .. code-block:: bash

        python -m ensurepip --upgrade

   - For macOS/Linux, you might need to use `python3` instead of `python`:

     .. code-block:: bash

        python3 -m ensurepip --upgrade

5. Update pip (Recommended)
---------------------------
   - It is a good practice to keep `pip` updated. Run:

     .. code-block:: bash

        pip install --upgrade pip

   - Verify the update by running:

     .. code-block:: bash

        pip --version

6. Install a Code Editor (Optional)
-----------------------------------
   - For a better coding experience, download and install a code editor like Visual Studio Code (https://code.visualstudio.com/).

7. Write and Run Your First Python Script
-----------------------------------------
   - Open a terminal or your code editor.
   - Create a new file with the `.py` extension (e.g., `hello.py`).
   - Add the following code to the file:

     .. code-block:: python

        print("Hello, Python!")

   - Run the script by executing:

     .. code-block:: bash

        python hello.py

   - If everything is set up correctly, you should see `Hello, Python!` printed in the terminal.

You have now successfully installed Python and verified its functionality.


