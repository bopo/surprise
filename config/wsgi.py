# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'verdors'))

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

# from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
# application = Sentry(application)
