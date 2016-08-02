# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import psycopg2

from .base import BASE_DIR

DEFAULT_CHARSET = 'utf-8'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'database', 'db.sqlite3'),
    },
    'mysql': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': 'config/mysql.conf',
        },
    },
    'postgresql': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'backend',
        'USER': 'backend',
        'PASSWORD': 'backend',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'OPTIONS': {
            'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
            'client_encoding': 'UTF8',
        },  'timezone': 'UTC',
    },
    'oracle': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'xe',
        'USER': 'a_user',
        'PASSWORD': 'a_password',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'threaded': True,
            'use_returning_into': False,
        },
    },
}
