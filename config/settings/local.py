# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from psycopg2.extensions import ISOLATION_LEVEL_SERIALIZABLE

try:
    from .base import *
except ImportError, e:
    raise e

DEBUG = env.bool("DJANGO_DEBUG", True)

INSTALLED_APPS += (
    # 'rest_framework_swagger',
    "sslserver",
    # 'cachalot',
    # 'django_q',
    # 'django_baker',
    # "debug_toolbar",
    #     'django_coverage',
    #     'django_extensions',
    #     'django_baker',
    #     'django_nose',
    #     'django_rest_framework_generator',
    #     'reversion',
    #     "categories",
    #     "categories.editor",
    #     'examples',
    #     'notifications',
    #     'allauth',
    #     'oauth_provider',
)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, '..', 'database', 'db.sqlite3'),
#     },
# }

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

if DEBUG:
    INSTALLED_APPS += ('debug_toolbar', 'raven.contrib.django.raven_compat',)
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    DEBUG_TOOLBAR_CONFIG = {'JQUERY_URL': '//cdn.bootcss.com/jquery/2.1.4/jquery.min.js'}

    import raven

    RAVEN_CONFIG = {
        'dsn': 'http://e4899f2e02c44585b3f0243af059ffce:c1bdb8f4725c4d3683af484a76cc76ad@10.7.7.100:9000/2',
        # 'release': raven.fetch_git_sha(os.path.dirname(__file__)),
    }

    # DEBUG_TOOLBAR_PANELS = ('cachalot.panels.CachalotPanel',)
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        # 'handlers': {
        #     'console': {
        #         'level': 'DEBUG',
        #         'class': 'logging.StreamHandler',
        #         # 'class': 'logging.handlers.RotatingFileHandler',
        #         # 'filename': os.path.join('runtime', 'debug.log'),
        #         # 'maxBytes': 1024 * 1024 * 5,  # 5 MB
        #         # 'backupCount': 5,
        #         # # 'formatter': 'standard',
        #     },
        # },
        # 'default': {
        #     'level': 'DEBUG',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': os.path.join('runtime', 'debug.log'),
        #     'maxBytes': 1024 * 1024 * 5,  # 5 MB
        #     'backupCount': 5,
        #     'formatter': 'standard',
        # },
        # 'loggers': {
        #     'django.db.backends': {
        #         'handlers': ['console'],
        #         'propagate': True,
        #         'level': 'DEBUG',
        #     },
        # }

    }

else:
    from .cache import *

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

# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
#     },
# }

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
#
# CACHE_BACKEND = 'dummy:///'

# USER_DETAILS_SERIALIZER = 'accounts.UserDetailsSerializer'
# REST_AUTH_SERIALIZERS = {
#     # 'LOGIN_SERIALIZER': 'path.to.custom.LoginSerializer',
#     # 'TOKEN_SERIALIZER': 'path.to.custom.TokenSerializer',
#     'USER_DETAILS_SERIALIZER': 'restful.contrib.account.serializers.AccountDetailsSerializer',
# }

# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Test runner
# TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'
# TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'

# try:
#     from .logs import *
# except ImportError, e:
#     raise e

# SECURE_SSL_REDIRECT = False
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')