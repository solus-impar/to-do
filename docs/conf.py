from recommonmark.parser import CommonMarkParser

project = 'planner'
copyright = '2018, Michael Canoy'
author = 'Michael Canoy'

version = ''
release = '0.0.1'

extensions = []
source_suffix = '.md'
source_parsers = {
    '.md': CommonMarkParser
}
master_doc = 'index'

language = None

pygments_style = 'sphinx'
html_theme = 'alabaster'
