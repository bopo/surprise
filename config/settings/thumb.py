# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import INSTALLED_APPS

INSTALLED_APPS += ('easy_thumbnails',)

THUMBNAIL_ALIASES = {
    '': {
        'avatar': {'size': (50, 50), 'crop': True},
    },
}

THUMB_LIST = '500x500'
THUMB_DETAIL = '800x800'
