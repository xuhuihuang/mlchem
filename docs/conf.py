import os, sys
import shutil


project = "MLCHEM"
copyright = "2025, Xuhui Huang"
release = 'v0.1'
github_url = "https://github.com/xuhuihuang/mlchem"


# absolute path to docs/
docdir = os.path.dirname(os.path.abspath(__file__))
# absolute path to project root
projectdir = os.path.dirname(docdir)

########################
# customize extensions #
########################
sys.path.insert(0, os.path.abspath('sphinxext'))
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx_codeautolink",
    # "sphinx_gallery.gen_gallery",
    "sphinx_gallery.load_style",
    "nbsphinx",
    "sphinx.ext.mathjax",
    # "notebook_sphinxext", # custom sphinx extension
    # "myst_nb"
]

# the documentation of the follwoing projects are generated via sphinx_codeautolink extension:
intersphinx_mapping = {
    'IPython': ('https://ipython.readthedocs.io/en/stable/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'python': ('https://docs.python.org/3/', None),
}

# doc theme
html_theme = 'furo'

# Furo theme options with GitHub integration
html_context = {
    "github_url": "https://github.com/xuhuihuang/mlchem",
    "github_user": "xuhuihuang",
    "github_repo": "mlchem",
    "github_version": "main",
    "doc_path": "docs/",
    "repo_url": "https://github.com/xuhuihuang/mlchem",
    "repo_name": "MLCHEM",
}

html_logo = '_static/figs/logo.png'

## nbsphinx config
nbsphinx_execute = "never"
nbsphinx_allow_errors = True
nbsphinx_codecell_lexer = "none"
# Suppress highlighting warnings for multiline shell commands
suppress_warnings = ['misc.highlighting_failure']

# add default notebook metadata
sphinx_gallery_conf = {
    "default_thumb_file": "_static/figs/cover_img.png",
    "thumbnail_size": (150, 150),
}

# add open in colab badger
nbsphinx_prolog = r"""
.. raw:: html

    <div class="colab-button">
        <a href="https://colab.research.google.com/github/xuhuihuang/mlchem/blob/main/{{ env.doc2path(env.docname, base=None) }}" target="_blank">
            <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open in Colab">
        </a>
    </div>
"""

source_suffix = ".rst"
templates_path = ['_templates']
exclude_patterns = [
    "build", # exclude build directory
    "GALLERY_HEADER.rst",
    "**/GALLERY_HEADER.rst"
]

html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_show_sourcelink = False

#############################
# copy raw sources to docs/ #
#############################

def _copy_raw_sources(app):
    mapping = {
        os.path.join(projectdir, "examples"): os.path.join(docdir, "examples"),
        os.path.join(projectdir, "lectures"): os.path.join(docdir, "_static", "lectures"),
        # os.path.join(projectdir, "homeworks"): os.path.join(docdir, "homeworks"), # for notebook compiling
        os.path.join(projectdir, "homeworks"): os.path.join(docdir, "_static", "homeworks"), # for pdf rendering
    }
    for src, dst in mapping.items():
        if not os.path.isdir(src):
            continue
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)

    # copy homework notebooks to be rendered
    hw_notebook_dir = os.path.join(docdir, "homeworks")
    if os.path.exists(hw_notebook_dir):
        shutil.rmtree(hw_notebook_dir)
    
    homeworks_dir = os.path.join(docdir, "_static", "homeworks")
    if os.path.exists(homeworks_dir):
        for root, _, files in os.walk(homeworks_dir):
            for file in files:
                if file.endswith('.ipynb'):
                    src = os.path.join(root, file)
                    # create relative path from homeworks_dir to maintain directory structure
                    rel_path = os.path.relpath(root, homeworks_dir)
                    dst_dir = os.path.join(hw_notebook_dir, rel_path)
                    dst = os.path.join(dst_dir, file)
                    
                    # create destination directory if it doesn't exist
                    os.makedirs(dst_dir, exist_ok=True)
                    
                    # copy notebook file
                    if not os.path.exists(dst):
                        shutil.copy2(src, dst)

#########
# setup #
#########
def setup(app):
    app.connect("builder-inited", _copy_raw_sources)
