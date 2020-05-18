#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'zst123'
SITENAME = "Manzel's Blog"
SITEURL = 'https://blog.manzelseet.com'

THEME = 'themes/tuxlite_zf'
PATH = 'content'

TIMEZONE = 'Asia/Singapore'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (
#    ('a', 'b'),
#)

# Social widget
SOCIAL = (
    ('Portfolio', 'https://manzelseet.com'),
    ('Github', 'https://github.com/zst123'),
    ('LinkedIn', 'https://www.linkedin.com/in/manzelseet/'),
)

DEFAULT_PAGINATION = False

STATIC_PATHS = ['downloads']
#ARTICLE_PATHS = ['blog']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True