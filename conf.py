# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TechDocs'
copyright = '2024, Oleh_Shynkarenko'
author = 'Oleh_Shynkarenko'
release = '23.12.24'

import sys
import os

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_tabs.tabs",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinxcontrib.video",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options
html_theme_options = {
    # if we have a html_logo below, this shows /only/ the logo with no title text
    "logo_only": True,
    # Collapse navigation (False makes it tree-like)
    "collapse_navigation": False,
    # Remove version and language picker beneath the title
    "version_selector": False,
    "language_selector": False,
    # Set Flyout menu to attached
    "flyout_display": "attached",
}

# Path to the static files
html_static_path = ['_static']

# Logo configuration
html_logo = "_static/my_logo.png"

# Link the logo to the main page
html_theme_options = {
    "logo_only": True,  # Display only the logo, not the project name
    "style_nav_header_background": "#2980B9",  # Optional: Customize sidebar header background color
}

# Ensure the logo links to the main page
html_context = {
    "display_github": False,  # Optional: Add GitHub link settings here
    "current_version": "",
    "current_page": "",
}

html_css_files = [
    "custom.css",
]
