# Configuration file for the Sphinx documentation builder.

project = "RAVEN API"
author = "AI4Secure"
copyright = "2026, AI4Secure"
release = "2.0"
version = "2.0"

extensions = [
    "sphinx_rtd_theme",
    "sphinx_copybutton",
    "sphinxcontrib.httpdomain",
    "sphinxcontrib.openapi",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "titles_only": False,
}
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sourcelink = False
html_title = "RAVEN API Documentation"

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

http_strict_mode = False

# -- Base URL placeholder (TBD) ------------------------------------------------
# Change this value once the production URL is finalized.
raven_base_url = "https://<BASE_URL_TBD>"

rst_epilog = f"""
.. |base_url| replace:: {raven_base_url}
"""
