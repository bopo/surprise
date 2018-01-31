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

# DOWNLOAD_ANDROID = 'https://www.pgyer.com/wzTi'
# DOWNLOAD_ANDROID = 'http://api.gjingxi.com/media/downloads/android.apk'
DOWNLOAD_ANDROID = 'http://url.cn/2Hw1ncX'
DOWNLOAD_IOS = 'https://itunes.apple.com/cn/app/gou-jing-xi/id1089420214?mt=8'
DOWNLOAD_URL = 'http://a.app.qq.com/o/simple.jsp?pkgname=com.surprisebuy.viewbrand'


# 1、taobao_tae_BaichuanTradeCreated
# 创建订单消息(下单未付款)，订单状态(order_status)是7
# 2、taobao_tae_BaichuanTradeSuccess
# 交易成功消息(确认收货后)，订单状态(order_status)是6
    # 3、taobao_tae_BaichuanTradeRefundCreated
# 买家点击退款按钮后促发
# 4、taobao_tae_BaichuanTradeRefundSuccess
# 退款成功，没有订单状态
        # 5、taobao_tae_BaichuanTradePaidDone
        # 付款成功(下单已付款)，订单状态(order_status)是2
# 6、taobao_tae_BaichuanTradeClosed
# 交易关闭(包括退款后交易关闭和创建订单后交易关闭)，
# order_status为4是退款后交易关闭，
# order_status为8是创建订单后交易关闭

ORDER_STATUS = (
    ('2', '付款成功'),
    ('7', '下单未付款'),
    ('6', '确认收货后'),
    ('4', '退款后交易关闭'),
    ('8', '创建订单后交易关闭'),
)

GENDER_CHOICES = (('male', '男'), ('female', '女'))