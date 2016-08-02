# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE

try:
    from .base import *
except ImportError, e:
    raise e


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'surprise',
        'USER': 'surprise',
        'PASSWORD': 'secret',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'OPTIONS': {
            'isolation_level': ISOLATION_LEVEL_SERIALIZABLE,
            'client_encoding': 'UTF8',
        },
        'timezone': 'UTC',
    }
}


# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': '127.0.0.1:6379',
#         'OPTIONS': {
#             'DB': 0,
#             'PASSWORD': '',
#             'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
#             'CONNECTION_POOL_CLASS_KWARGS': {
#                 'max_connections': 50,
#                 'timeout': 20,
#             }
#         },
#     },
# }

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }



STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# CACHE_BACKEND = 'redis_cache.cache://127.0.0.1:6379'
