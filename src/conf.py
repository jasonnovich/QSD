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

project = 'DVG Quick Start Guide'
copyright = '2020, Jason Novich'
author = 'Jason Novich'

# The full version, including alpha/beta/rc tags
release = '.01'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# import sphinx_rtd_theme
extensions = [
    "sphinx_rtd_theme",
    "rst2pdf.pdfbuilder",
    'sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', '_static']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# -- Options for PDF output --------------------------------------------------

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document. For example:
#
# ('index', 'MyProject', 'My Project', 'Author Name', {'pdf_compressed': True})
#
# would mean that specific document would be compressed
# regardless of the global 'pdf_compressed' setting.

pdf_documents = [
    ('index', 'DVG Quick Start Guide', 'DVG Quick Start Guide', 'Author Name'),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx', 'kerning', 'a4', 'styles', 'jasonBase']

# A list of folders to search for stylesheets. Example:
pdf_style_path = ['.', '_styles']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
# pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']

# Language to be used for hyphenation support
pdf_language = "en_US"

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
# pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
pdf_break_level = 1

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
# pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
# pdf_verbosity = 0

# If false, no index is generated.
# pdf_use_index = True

# If false, no modindex is generated.
# pdf_use_modindex = True

# If false, no coverpage is generated.
pdf_use_coverpage = True

# Name of the cover page template to use
pdf_cover_template = 'DVG_Cover.tmpl'

# Documents to append as an appendix to all manuals.
# pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
# pdf_splittables = False

# Set the default DPI for images
# pdf_default_dpi = 72

# Enable rst2pdf extension modules
# pdf_extensions = []

# Page template name for "regular" pages
pdf_page_template = 'oneColumn'

# Show Table Of Contents at the beginning?
pdf_use_toc = True

# How many levels deep should the table of contents be?
pdf_toc_depth = 4

# Add section number to section references
pdf_use_numbered_links = True

# Background images fitting mode
pdf_fit_background_mode = 'scale'

# Repeat table header on tables that cross a page boundary?
pdf_repeat_table_rows = True

