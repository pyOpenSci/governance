# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'governance'
copyright = '2023, pyOpenSci'
author = 'pyOpenSci'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_nb",
    # "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx"
]

# colon fence for card support in md
myst_enable_extensions = ["colon_fence"]


# Link to our repo for easy PR/ editing

html_theme_options = {
    "announcement": "<p><a href='https://www.pyopensci.org/software-peer-review/about/intro.html'>Submit Your Python Package for Peer Review - Learn More!</a></p>",
    "external_links": [
        {
            "url": "https://www.pyopensci.org",
            "name": "pyOpenSci Website",
        },
        {
            "url": "https://www.pyopensci.org/python-package-guide",
            "name": "Packaging Guide",
        },
        {
            "url": "https://pyopensci.org/python-package-guide",
            "name": "Peer Review Guide",
        },
    ],
    "header_links_before_dropdown": 4,
    "use_edit_page_button": True,
    "show_toc_level": 1,
    "navbar_align": "left",  # [left, content, right] For testing that the navbar items align properly
    "github_url": "https://github.com/pyopensci/governance",
    "twitter_url": "https://twitter.com/pyopensci",
}

html_context = {
    "github_user": "pyopensci",
    "github_repo": "governance",
    "github_version": "main",
}

#     "repository_url": "https://github.com/pyopensci/governance",
#     "use_repository_button": True,
#     "google_analytics_id": "UA-141260825-1",
#     "external_links": [
#       {"name": "link-one-name", "url": "https://pyopensci.org"},
#       {"name": "link-two-name", "url": "https://pyopensci.org"}
#   ],
#   "announcement": "✨ <a href="https://www.pyopensci.org/software-peer-review/about/intro.html">Learn more about our peer review process</a> ✨"
# }

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".github",
    ".nox",
    "README.md",
    "reference/2018-2020-orig-meeting-notes"
    ]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_static_path = ["_static"]
html_title = "pyOpenSci Governance"
html_logo = "images/logo/logo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
