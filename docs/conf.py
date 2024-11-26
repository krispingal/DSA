# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

# sys.path.insert(0, os.path.abspath(os.path.join("..", "..", "src")))
sys.path.insert(0, os.path.abspath("../src"))

project = "dsa"
copyright = "2024, Krishna Babuji"
author = "Krishna Babuji"
release = "0.1"

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
]

autodoc_default_options = {
    "members": True,  # Include module/class members
    "undoc-members": True,  # Include members without docstrings
    "show-inheritance": True,  # Show class inheritance
}


autosummary_generate = True
autodoc_typehints = "description"
autodoc_member_order = "bysource"

autodoc_typehints = "description"

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False  # Set True if using NumPy-style docstrings
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_notes = True
napoleon_use_rtype = False  # Avoid redundant "Returns" type
napoleon_preprocess_types = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
