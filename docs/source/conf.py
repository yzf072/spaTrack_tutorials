import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = 'spaTrack_tutorials'
copyright = '2023, BGI'
author = 'BGI'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'nbsphinx',
    'myst_parser',
]

# -- Options for HTML output -------------------------------------------------
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
