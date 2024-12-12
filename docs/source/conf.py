# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Tkinter GUI App'
copyright = '2024, Alaa'
author = 'Alaa'
release = 'December 11'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',    # Automatically document code
    'sphinx.ext.viewcode',   # Include source code in documentation
    'sphinx.ext.napoleon',   # Support for Google/NumPy-style docstrings
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']  # Common exclude patterns

language = 'python'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'  # You can change this to 'alabaster' if preferred
html_static_path = ['_static']

# -- Path setup --------------------------------------------------------------
# If your Python files are outside the `docs` directory, add their location to sys.path.
import os
import sys
sys.path.insert(0, os.path.abspath("C:\\Users\\student\\Desktop\\Lab3files"))
