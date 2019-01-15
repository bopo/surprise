# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib
from sys import version_info

import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from six import string_types

if version_info < (2, 7):
    from django.utils.importlib import import_module
else:
    from importlib import import_module


def import_callable(path_or_callable):
    if hasattr(path_or_callable, '__call__'):
        return path_or_callable
    else:
        assert isinstance(path_or_callable, string_types)
        package, attr = path_or_callable.rsplit('.', 1)
        return getattr(import_module(package), attr)


def smsbao(mobile, code):
    ERRORS_CODE = {
        '30': '密码错误',
        '40': '账号不存在',
        '41': '余额不足',
        '42': '帐号过期',
        '43': 'IP地址限制',
        '50': '内容含有敏感词',
        '51': '手机号码不正确',
    }

    username = 'ibopo'
    password = 'b87225300'
    url = 'http://api.smsbao.com/sms?u=%(USERNAME)s&p=%(PASSWORD)s&m=%(PHONE)s&c=%(CONTENT)s'

    m2 = hashlib.md5()
    m2.update(password)
    password = m2.hexdigest()

    params = {'USERNAME': username, 'PASSWORD': password, 'PHONE': mobile, 'CONTENT': code}
    req = requests.get(url=url % params, params={'mobile': mobile, 'code': code})

    return ERRORS_CODE.get(req.content)


def user_field(user, field, *args):
    """
    Gets or sets (optional) user model fields. No-op if fields do not exist.
    """
    if field and hasattr(user, field):
        if args:
            # Setter
            v = args[0]
            if v:
                User = get_user_model()
                v = v[0:User._meta.get_field(field).max_length]
            setattr(user, field, v)
        else:
            # Getter
            return getattr(user, field)


def user_username(user, *args):
    return user_field(user, settings.USER_MODEL_USERNAME_FIELD, *args)


def user_email(user, *args):
    return user_field(user, settings.USER_MODEL_EMAIL_FIELD, *args)


from django.utils import six

try:
    import importlib
except ImportError:
    from django.utils import importlib  # noqa


def import_attribute(path):
    assert isinstance(path, six.string_types)
    pkg, attr = path.rsplit('.', 1)
    ret = getattr(importlib.import_module(pkg), attr)
    return ret
