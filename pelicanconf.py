#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Chris Cronin'
SITENAME = "Chris' Blog"
SITEURL = ''
SITETITLE = AUTHOR
SITESUBTITLE = 'MBA & Machine Learning Engineer'
SITELOGO = SITEURL + '/images/profshot.jpg'
FAVICON = SITEURL + '/images/dodgest_logo3.jpg'

THEME = '/Users/Cronin/pelican-themes/Flex-master'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True

MENUITEMS =  (('Projects','/category/projects.html'),
             ('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

# Blogroll
LINKS = (('Projects','/category/projects.html'))

# Social widget
SOCIAL = (('linkedin',  'https://www.linkedin.com/in/cvcronin'),
          ('github', 'https://github.com/ccronin51'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = ['jinja2.ext.i18n']

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']
