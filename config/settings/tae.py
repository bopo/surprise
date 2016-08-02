# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from .local import *
except ImportError, e:
    raise e

DEBUG = True
