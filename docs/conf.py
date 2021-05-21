# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Astropy documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default. Some values are defined in
# the global Astropy configuration which is loaded here before anything else.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('..'))
# IMPORTANT: the above commented section was generated by sphinx-quickstart, but
# is *NOT* appropriate for astropy or Astropy affiliated packages. It is left
# commented out with this explanation to make it clear why this should not be
# done. If the sys.path entry above is added, when the astropy.sphinx.conf
# import occurs, it will import the *source* version of astropy instead of the
# version installed (if invoked as "make html" or directly with sphinx), or the
# version in the build directory.
# Thus, any C-extensions that are needed to build the documentation will *not*
# be accessible, and the documentation will not build correctly.
# See sphinx_astropy.conf for which values are set there.

import os
import sys
import configparser
from datetime import datetime

from packaging.requirements import Requirement

try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata

try:
    from sphinx_astropy.conf.v1 import *  # noqa
except ImportError:
    print('ERROR: the documentation requires the sphinx-astropy package to be installed')
    sys.exit(1)


plot_rcparams = {}
plot_rcparams['figure.figsize'] = (6, 6)
plot_rcparams['savefig.facecolor'] = 'none'
plot_rcparams['savefig.bbox'] = 'tight'
plot_rcparams['axes.labelsize'] = 'large'
plot_rcparams['figure.subplot.hspace'] = 0.5

plot_apply_rcparams = True
plot_html_show_source_link = False
plot_formats = ['png', 'svg', 'pdf']
# Don't use the default - which includes a numpy and matplotlib import
plot_pre_code = ""

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.7'

# To perform a Sphinx version check that needs to be more specific than
# major.minor, call `check_sphinx_version("X.Y.Z")` here.
check_sphinx_version("1.2.1")  # noqa: F405

# The intersphinx_mapping in sphinx_astropy.sphinx refers to astropy for
# the benefit of other packages who want to refer to objects in the
# astropy core.  However, we don't want to cyclically reference astropy in its
# own build so we remove it here.
del intersphinx_mapping['astropy']  # noqa: F405

# add any custom intersphinx for astropy
intersphinx_mapping['astropy-dev'] = ('https://docs.astropy.org/en/latest/', None)  # noqa: F405
intersphinx_mapping['pyerfa'] = ('https://pyerfa.readthedocs.io/en/stable/', None)  # noqa: F405
intersphinx_mapping['pytest'] = ('https://pytest.readthedocs.io/en/stable/', None)  # noqa: F405
intersphinx_mapping['ipython'] = ('https://ipython.readthedocs.io/en/stable/', None)  # noqa: F405
intersphinx_mapping['pandas'] = ('https://pandas.pydata.org/pandas-docs/stable/', None)  # noqa: F405, E501
intersphinx_mapping['sphinx_automodapi'] = ('https://sphinx-automodapi.readthedocs.io/en/stable/', None)  # noqa: F405, E501
intersphinx_mapping['packagetemplate'] = ('https://docs.astropy.org/projects/package-template/en/latest/', None)  # noqa: F405, E501
intersphinx_mapping['h5py'] = ('http://docs.h5py.org/en/stable/', None)  # noqa: F405

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns.append('_templates')  # noqa: F405
exclude_patterns.append('changes')  # noqa: F405
exclude_patterns.append('_pkgtemplate.rst')  # noqa: F405
exclude_patterns.append('**/*.inc.rst')  # .inc.rst mean *include* files, don't have sphinx process them  # noqa: F405, E501

# Add any paths that contain templates here, relative to this directory.
if 'templates_path' not in locals():  # in case parent conf.py defines it
    templates_path = []
templates_path.append('_templates')


extensions += ["sphinx_changelog"]  # noqa: F405

# Grab minversion from setup.cfg
setup_cfg = configparser.ConfigParser()
setup_cfg.read(os.path.join(os.path.pardir, 'setup.cfg'))
__minimum_python_version__ = setup_cfg['options']['python_requires'].replace('>=', '')
project = u'Astropy'

min_versions = {}
for line in importlib_metadata.requires('astropy'):
    req = Requirement(line.split(';')[0])
    min_versions[req.name.lower()] = str(req.specifier)


# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
with open("common_links.txt", "r") as cl:
    rst_epilog += cl.read().format(minimum_python=__minimum_python_version__,
                                   **min_versions)

# Whether to create cross-references for the parameter types in the
# Parameters, Other Parameters, Returns and Yields sections of the docstring.
numpydoc_xref_param_type = True

# Words not to cross-reference. Most likely, these are common words used in
# parameter type descriptions that may be confused for classes of the same
# name.
numpydoc_xref_ignore = {
    'type', 'optional', 'default', 'or', 'of', 'method', 'instance', "like",
    "class", 'subclass', "keyword-only", "default", "thereof", "mixin",
    # needed in subclassing numpy  # TODO! revisit
    "Arguments", "Path",
    # TODO! not need to ignore.
    "flag", "bits",
}

# Mappings to fully qualified paths (or correct ReST references) for the
# aliases/shortcuts used when specifying the types of parameters.
# Numpy provides some defaults
# https://github.com/numpy/numpydoc/blob/b352cd7635f2ea7748722f410a31f937d92545cc/numpydoc/xref.py#L62-L94
# so we only need to define Astropy-specific x-refs
numpydoc_xref_aliases = {
    # ultra-general
    "-like": ":term:`-like`",
    # python & adjacent
    "file-like": ":term:`python:file-like object`",
    "file": ":term:`python:file object`",
    "iterator": ":term:`python:iterator`",
    "path-like": ":term:`python:path-like object`",
    "module": ":term:`python:module`",
    "buffer-like": ":term:buffer-like",
    "function": ":term:`python:function`",
    # for matplotlib
    "color": ":term:`color`",
    # for numpy
    "ints": ":class:`python:int`",
    # for astropy
    "unit-like": ":term:`unit-like`",
    "quantity-like": ":term:`quantity-like`",
    "angle-like": ":term:`angle-like`",
    "table-like": ":term:`table-like`",
    "time-like": ":term:`time-like`",
    "frame-like": ":term:`frame-like`",
    "coordinate-like": ":term:`coordinate-like`",
    "number": ":term:`number`",
    "Representation": ":class:`~astropy.coordinates.BaseRepresentation`",
    "writable": ":term:`writable file-like object`",
    "readable": ":term:`readable file-like object`",
    "BaseHDU": ":doc:`HDU </io/fits/api/hdus>`"
}
# Astropy units physical types
from astropy.units.physical import _units_and_physical_types
numpydoc_xref_physical_type_aliases = {}
for _, ptypes in _units_and_physical_types:
    ptypes = {ptypes} if isinstance(ptypes, str) else ptypes
    for ptype in ptypes:
        key = f"'{ptype}'"
        val = f":ref:`'{ptype}' <{ptype}>`"
        numpydoc_xref_physical_type_aliases[key] = val

numpydoc_xref_aliases.update(numpydoc_xref_physical_type_aliases)


# -- Project information ------------------------------------------------------

author = u'The Astropy Developers'
copyright = f'2011–{datetime.utcnow().year}, ' + author

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The full version, including alpha/beta/rc tags.
release = importlib_metadata.version(project)
# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# Only include dev docs in dev version.
dev = 'dev' in release
if not dev:
    exclude_patterns.append('development/*')  # noqa: F405
    exclude_patterns.append('testhelpers.rst')  # noqa: F405

# -- Options for the module index ---------------------------------------------

modindex_common_prefix = ['astropy.']


# -- Options for HTML output ---------------------------------------------------

# A NOTE ON HTML THEMES
#
# The global astropy configuration uses a custom theme,
# 'bootstrap-astropy', which is installed along with astropy. The
# theme has options for controlling the text of the logo in the upper
# left corner. This is how you would specify the options in order to
# override the theme defaults (The following options *are* the
# defaults, so we do not actually need to set them here.)

# html_theme_options = {
#    'logotext1': 'astro',  # white,  semi-bold
#    'logotext2': 'py',     # orange, light
#    'logotext3': ':docs'   # white,  light
#    }

# A different theme can be used, or other parts of this theme can be
# modified, by overriding some of the variables set in the global
# configuration. The variables set in the global configuration are
# listed below, commented out.

# Add any paths that contain custom themes here, relative to this directory.
# To use a different custom theme, add the directory containing the theme.
# html_theme_path = []

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes. To override the custom theme, set this to the
# name of a builtin theme or the name of a custom theme in html_theme_path.
# html_theme = None

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = ''

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = ''

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = f'{project} v{release}'

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'

# A dictionary of values to pass into the template engine’s context for all pages.
html_context = {
    'to_be_indexed': ['stable', 'latest'],
    'is_development': dev
}

# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [('index', project + '.tex', project + u' Documentation',
                    author, 'manual')]

latex_logo = '_static/astropy_logo.pdf'


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [('index', project.lower(), project + u' Documentation',
              [author], 1)]

# Setting this URL is requited by sphinx-astropy
github_issues_url = 'https://github.com/astropy/astropy/issues/'
edit_on_github_branch = 'main'

# Enable nitpicky mode - which ensures that all references in the docs
# resolve.

nitpicky = True
# This is not used. See docs/nitpick-exceptions file for the actual listing.
nitpick_ignore = []

for line in open('nitpick-exceptions'):
    if line.strip() == "" or line.startswith("#"):
        continue
    dtype, target = line.split(None, 1)
    target = target.strip()
    nitpick_ignore.append((dtype, target))

# -- Options for the Sphinx gallery -------------------------------------------

try:
    import warnings

    import sphinx_gallery  # noqa: F401
    extensions += ["sphinx_gallery.gen_gallery"]  # noqa: F405

    sphinx_gallery_conf = {
        'backreferences_dir': 'generated/modules',  # path to store the module using example template  # noqa: E501
        'filename_pattern': '^((?!skip_).)*$',  # execute all examples except those that start with "skip_"  # noqa: E501
        'examples_dirs': f'..{os.sep}examples',  # path to the examples scripts
        'gallery_dirs': 'generated/examples',  # path to save gallery generated examples
        'reference_url': {
            'astropy': None,
            'matplotlib': 'https://matplotlib.org/',
            'numpy': 'https://numpy.org/doc/stable/',
        },
        'abort_on_example_error': True
    }

    # Filter out backend-related warnings as described in
    # https://github.com/sphinx-gallery/sphinx-gallery/pull/564
    warnings.filterwarnings("ignore", category=UserWarning,
                            message='Matplotlib is currently using agg, which is a'
                                    ' non-GUI backend, so cannot show the figure.')

except ImportError:
    sphinx_gallery = None


# -- Options for linkcheck output -------------------------------------------
linkcheck_retry = 5
linkcheck_ignore = ['https://journals.aas.org/manuscript-preparation/',
                    'https://maia.usno.navy.mil/',
                    'https://www.usno.navy.mil/USNO/time/gps/usno-gps-time-transfer',
                    'https://aa.usno.navy.mil/publications/docs/Circular_179.php',
                    'http://data.astropy.org',
                    r'https://github\.com/astropy/astropy/(?:issues|pull)/\d+']
linkcheck_timeout = 180
linkcheck_anchors = False

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
html_extra_path = ['robots.txt']


def rstjinja(app, docname, source):
    """Render pages as a jinja template to hide/show dev docs. """
    # Make sure we're outputting HTML
    if app.builder.format != 'html':
        return
    files_to_render = ["index", "install"]
    if docname in files_to_render:
        print(f"Jinja rendering {docname}")
        rendered = app.builder.templates.render_string(
            source[0], app.config.html_context)
        source[0] = rendered


def resolve_astropy_and_dev_reference(app, env, node, contnode):
    """
    Reference targets for ``astropy:`` and ``astropy-dev:`` are special cases.

    Documentation links in astropy can be set up as intersphinx links so that
    affiliate packages do not have to override the docstrings when building
    the docs.

    If we are building the development docs it is a local ref targeting the
    label ``astropy-dev:<label>``, but for stable docs it should be an
    intersphinx resolution to the development docs.

    See https://github.com/astropy/astropy/issues/11366
    """
    # should the node be processed?
    reftarget = node.get('reftarget')  # str or None
    if str(reftarget).startswith('astropy:'):
        # This allows Astropy to use intersphinx links to itself and have
        # them resolve to local links. Downstream packages will see intersphinx.
        # TODO! deprecate this if sphinx-doc/sphinx/issues/9169 is implemented.
        process, replace = True, 'astropy:'
    elif dev and str(reftarget).startswith('astropy-dev:'):
        process, replace = True, 'astropy-dev:'
    else:
        process, replace = False, ''

    # make link local
    if process:
        reftype = node.get('reftype')
        refdoc = node.get('refdoc', app.env.docname)
        # convert astropy intersphinx targets to local links.
        # there are a few types of intersphinx link patters, as described in
        # https://docs.readthedocs.io/en/stable/guides/intersphinx.html
        reftarget = reftarget.replace(replace, '')
        if reftype == "doc":  # also need to replace the doc link
            node.replace_attr("reftarget", reftarget)
        # Delegate to the ref node's original domain/target (typically :ref:)
        try:
            domain = app.env.domains[node['refdomain']]
            return domain.resolve_xref(app.env, refdoc, app.builder,
                                       reftype, reftarget, node, contnode)
        except Exception:
            pass

        # Otherwise return None which should delegate to intersphinx


def setup(app):
    if sphinx_gallery is None:
        msg = ('The sphinx_gallery extension is not installed, so the '
               'gallery will not be built.  You will probably see '
               'additional warnings about undefined references due '
               'to this.')
        try:
            app.warn(msg)
        except AttributeError:
            # Sphinx 1.6+
            from sphinx.util import logging
            logger = logging.getLogger(__name__)
            logger.warning(msg)

    # Generate the page from Jinja template
    app.connect("source-read", rstjinja)
    # Set this to higher priority than intersphinx; this way when building
    # dev docs astropy-dev: targets will go to the local docs instead of the
    # intersphinx mapping
    app.connect("missing-reference", resolve_astropy_and_dev_reference,
                priority=400)
