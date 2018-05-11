#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Susanne Meerwald-Stadler'
SITENAME = u'smeerws'
SITEURL = ''
THEME = u'themes/pelican-cait'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'de'

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_CUSTOM_MENU = True

CUSTOM_MENUITEMS = (('VR-Tools', 'pages/vrpainting.html'),
                    ('Acryl', 'category/acryl.html'),
                    ('About Me', 'pages/contact.html'))

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/paulomiramor'),
          ('linkedin', 'http://www.linkedin.com/in/XXXXXXX'),
          ('github', 'https://github.com/EuPaulo'),)

DEFAULT_PAGINATION = 12

STATIC_PATHS = ['images', 'pdfs' , 'pages']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
