import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------
project = 'spaTrack_tutorials'
copyright = '2023, BGI'
author = 'BGI'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'nbsphinx',
    'myst_parser',
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

autosummary_generate = True
autodoc_member_order = 'bysource'
napoleon_include_init_with_doc = False
napoleon_numpy_docstring = True
napoleon_use_rtype = True
napoleon_use_param = True

templates_path = ['_templates']
exclude_patterns = []

intersphinx_mapping={
    'numpy': ('https://numpy.org/doc/stable/',None),
    'anndata': ('https://anndata.readthedocs.io/en/latest/',None),
    
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
