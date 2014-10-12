#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Weiqi Zhang'
SITENAME = u"WeiqiZhang"
SITEURL = 'http://wqzhang.com'
######################
#added by snooze
GOOGLE_ANALYTICS = 'UA-39331985-2'
THEME = "themes/my-pelican-bootstrap3"
RELATIVE_URLS = False	# True when developing
DISPLAY_CATEGORIES_ON_MENU = False
######################
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
'''
LINKS =  (('Pelican', 'http://getpelican.com/'),
          
          )'''

# Social widget
SOCIAL = (('Linkedin','https://www.linkedin.com/pub/weiqi-zhang/6a/688/64a'),
		('Github', 'https://github.com/SnoozeZ'),
		  )

DEFAULT_PAGINATION = 6

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
