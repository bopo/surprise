# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from .base import *
except ImportError, e:
    raise e

DEBUG = False
INSTALLED_APPS += (
    # 'examples',
    # 'reversion',
    # 'categories',
    # 'notifications',
    # 'debug_toolbar',
    # 'django_coverage',
    # 'categories.editor',
    # 'django_rest_framework_generator',

    'allauth',
    # 'oauth_provider',
    'django_extensions',
)

DEFAULT_CHARSET = 'utf-8'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'database', 'db.sqlite3'),
    },
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'moo',
#         'USER': 'bopo',
#         'PASSWORD': '87225300',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js'
}
# RELATION_MODELS = ['CategoryRelation']

# CATEGORIES_SETTINGS = {
#     'FK_REGISTRY': {
#         'app.AModel': 'category',
#         'app.MyModel': (
#             'primary_category',
#             {'name': 'secondary_category', 'related_name': 'mymodel_sec_cat'},)
#     },
#     'M2M_REGISTRY': {
#         'app.BModel': 'categories',
#         'app.MyModel': ('other_categories', 'more_categories',),
#     }
# }
#
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
#         'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
#     },
# }

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        'OPTIONS': {
            'DB': 0,
            'PASSWORD': '',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            }
        },
    },
}

CACHE_BACKEND = 'dummy:///'

# USER_DETAILS_SERIALIZER = 'accounts.UserDetailsSerializer'
# REST_AUTH_SERIALIZERS = {
#     # 'LOGIN_SERIALIZER': 'path.to.custom.LoginSerializer',
#     # 'TOKEN_SERIALIZER': 'path.to.custom.TokenSerializer',
#     'USER_DETAILS_SERIALIZER': 'restful.contrib.account.serializers.AccountDetailsSerializer',
# }

# Test runner
# TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'
# TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'
