# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import INSTALLED_APPS

INSTALLED_APPS += (
    'restful',
    'restful.contrib.runner',
    'restful.contrib.consumer',
    'restful.contrib.restauth',
    'restful.contrib.restauth.registration',

    'frontend',
    'imagekit',
    'easy_select2',
    'import_export',
    'reversion',
    # 'django_mobile',
)

TOP_APPKEY = '23255563'
TOP_SECRET = 'f7092fdb96f20625742d577820936b5c'

JPUSH_APPKEY = u'5432833aa78e771efca25be3'
JPUSH_SECRET = u'0ed88cbd56b67e96a9df7885'

WECHAT_APPKEY = 'wx25cb974381f02fa1'
WECHAT_SECRET = 'fe59d7ab30c2a96ebd086c4d09a1746f'

APPEND_SLASH = True
DEVICE_MAX_REG_NUMS = 5

TREND_URL = 'https://gupiao.baidu.com/stock/sh000001.html'

# app settings
BEST_RATE = 0.5
FIRST_RATE = 0.5

DOWNLOAD_ANDROID = 'https://www.pgyer.com/wzTi'
DOWNLOAD_IOS = 'https://itunes.apple.com/cn/app/gou-jing-xi/id1089420214?mt=8'
