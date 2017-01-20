#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cory Robinson'
SITENAME = u'SciProX'
SITEURL = 'http://sciprox.com'

PATH = 'content'

TIMEZONE = 'US/Central'

DEFAULT_LANG = u'en'

THEME = 'theme/pure'

# sidebar stuff
# TODO: set up some custom sidebar html stuff
SIDEBAR_NAME = 'Cory Robinson'
SIDEBAR_LOCATION = 'Houston, Texas'
SIDEBAR_SUBNAME = 'science | computing | data'

# post
ARTICLE_URL = 'posts/{date:%Y}-{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}-{date:%m}/{slug}/index.html'

# pages
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['pages']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github-square', 'https://github.com/creedr'),
          ('google-plus-square', 'https://plus.google.com/u/0/+CoryRobinson'),
          ('linkedin-square', 'https://www.linkedin.com/in/cory-robinson-93976a15/'),
          ('twitter-square', 'https://twitter.com/cory_rr'))

DEFAULT_PAGINATION = 10

# use custom domain name
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
