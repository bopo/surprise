# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import djcelery

from .base import INSTALLED_APPS


CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

djcelery.setup_loader()
# CELERY_ALWAYS_EAGER = True

INSTALLED_APPS += (
    'djcelery',
    'kombu.transport.django',
    # 'common.tasks.celery.Config',
)

# BROKER_URL = 'django://'
BROKER_URL = "redis://127.0.0.1:6379/0"
# BROKER_HOST = "localhost"
# BROKER_PORT = 5672
# BROKER_USER = "root"
# BROKER_PASSWORD = "root"
# BROKER_VHOST = "/"
