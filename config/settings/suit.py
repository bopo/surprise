# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from base import *

INSTALLED_APPS = ("suit",) + INSTALLED_APPS + ('suit_redactor', 'mptt',)

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'API内容管理系统',
    'HEADER_DATE_FORMAT': 'Y F j l',
    'HEADER_TIME_FORMAT': 'Y-m-d H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True,  # Default True

    # menu
    'SEARCH_URL': '/admin/auth/user/',
    'MENU_ICONS': {
        'sites': 'icon-leaf',
        'auth': 'icon-lock',
    },
    'MENU_OPEN_FIRST_CHILD': True,  # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': '认证', 'icon': 'icon-lock', 'models': ('user', 'group')},
    #     {'label': '资源管理', 'icon': 'icon-cog', 'models': ('restful.restauth', 'restful.stars','restful.brand')},
    #     {'label': '设置', 'icon': 'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': '支持', 'icon': 'icon-question-sign', 'url': '/admin/doc/'},
    # ),

    # misc
    'LIST_PER_PAGE': 15,
}
