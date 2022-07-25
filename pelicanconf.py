from pelican_jupyter import markup as nb_markup

AUTHOR = 'Ann Cooper'
SITENAME = 'Dev Slush Pile'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

PLUGINS = [nb_markup]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Sean Harrison', 'https://kruxia.gitlab.io/goodtech-is/'),
         ('The Caktus Group', 'https://www.caktusgroup.com/blog/'),
         )

# Social widget
SOCIAL = (('Nothing here yet', '#'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Jupyter
MARKUP = ('md', 'ipynb')
IGNORE_FILES = [".ipynb_checkpoints"]