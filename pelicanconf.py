#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Susanne Meerwald-Stadler'
SITENAME = u'[VR] Artist'
SITEURL = ''
SITEDESCRIPTION='Site Description'
SITESUBTITLE = 'Hi! Ich liebe es kreativ zu arbeiten, in jeder Realität, die mir zur Verfügung steht. Meine Werkzeuge reichen von Pinsel und Leinwand bis zum plastischen Gestalten mit Brille und Kreativprogramm in der virtuellen Realität.'
#SITESUBTITLE = 'VR [Artist]'
THEME = u'../pelican-themes/pelican-cait'

GOOGLE_ANALYTICS = 'UA-119698590-1'

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
		    ('VR-Photomalerei', 'category/vr-photomalerei.html'),
                    ('VR-Modellieren', 'category/vr-modellieren.html'),
                    ('VR-Werkzeuge', 'category/vr-werkzeuge.html'),
                    ('Über mich', 'pages/about.html'),
                    ('Sammelsurium', 'category/sammelsurium.html'),
                    ('Buy me a coffee', 'https://www.buymeacoffee.com/smeerws'),)

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

CONTACT_EMAIL = "hello@smeerws.at"

# Social widget swithced from social to contacts for Contact page
CONTACTS = (('twitter', 'https://twitter.com/smeerws'),
            ('linkedin', 'https://www.linkedin.com/in/susannestadler/'),
            ('github', 'https://github.com/smeerws'),
            ('bmc', 'https://www.buymeacoffee.com/smeerws'),
            ('poly', 'https://poly.google.com/user/deXEWo4P-yG'),
            ('sketchfab', 'https://sketchfab.com/smeerws'),)

DEFAULT_PAGINATION = 12

STATIC_PATHS = ['images', 'pdfs', 'pages']

PLUGIN_PATHS = ['plugins',]
PLUGINS = ['i18n_subsites',]

LOCALE = {'en_US.utf8', 'de_AT.utf8'}
DATE_FORMATS = {
    'en': ('en_US.utf8', '%A, %B %d, %Y'),
    'de': ('de_AT.utf8', '%A, %d. %B %Y'),
}

I18N_SUBSITES = {
    'en': {
    'SITESUBTITLE': 'Hi! I love it to work creatively, in every reality that is available to me. My tools range from brushes and canvas to sculptural design with VR glasses and creative programs in virtual reality.',
    'CUSTOM_MENUITEMS': (('Acrylic-Painting', 'category/acrylic-painting.html'),
		    ('VR-Photopainting', 'category/vr-photopainting.html'),
                    ('VR-Sculpting', 'category/vr-sculpting.html'),
                    ('VR-Tools', 'category/vr-tools.html'),
                    ('About me', 'pages/about.html'),
                    ('Ragbag', 'category/ragbag.html'),
                    ('Buy me a coffee', 'https://www.buymeacoffee.com/smeerws'),)
    }
}

def extract_trans(article, lang, default_lang, url):
    if hasattr(article, 'translations'):
        for trans in article.translations:
            if trans.lang == lang:
                return trans.url
        return url
    else:
        try: mi_from = I18N_SUBSITES[default_lang]['CUSTOM_MENUITEMS']
        except KeyError: mi_from = CUSTOM_MENUITEMS
        try: mi_to = I18N_SUBSITES[lang]['CUSTOM_MENUITEMS']
        except KeyError: mi_to = CUSTOM_MENUITEMS
        try:
            idx = [u for t, u in mi_from].index(article.url)
            return mi_to[idx][1]
        except:
            return url

JINJA_FILTERS = {
    'extract_trans': extract_trans,
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
