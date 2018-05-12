#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Susanne Meerwald-Stadler'
SITENAME = u'smeerws'
SITEURL = ''
SITESUBTITLE= 'Hallo! Mein Hintergrund ist Informatik mit dem Fokus auf User Experience (UX) Design. Ich liebe alles was mit Robotern, Augmented und Virtual Reality zu tun hat.  In letzter Zeit habe ich meine Leidenschaft für Kunst wiederentdeckt. Jetzt habe ich angefangen meine Faehigkeiten und meine Leidenschaft zu verbinden und die virtuelle Realitaet und ihre Moeglichkeiten zu erforschen. Wer mich dabei unterstützen moechte ist eingeladen mir eine Tasse Kaffee zu kaufen unter https://www.buymeacoffee.com/smeerws'
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

CUSTOM_MENUITEMS = (('Acryl-Malerei', 'category/acryl-malerei.html'),
		    ('VR-Malerei', 'category/vr-malerei.html'),
                    ('VR-Modellieren', 'category/vr-modellieren.html'),
                    ('VR-Werkzeuge', 'pages/vr-werkzeuge.html'),
                    ('Über mich', 'pages/uber-mich.html'),
                    ('Sammelsurium', 'pages/sammelsurium.html'),)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

CONTACT_EMAIL = "hello@smeerws.at"

# Social widget swithced from social to contacts for Contact page
CONTACTS = (('twitter', 'https://twitter.com/smeerws'),
          ('linkedin', 'https://www.linkedin.com/in/susannestadler/'),
          ('github', 'https://github.com/smeerws'),)

DEFAULT_PAGINATION = 12

STATIC_PATHS = ['images', 'pdfs' , 'pages']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
