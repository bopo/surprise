# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import versioning
from rest_framework.versioning import URLPathVersioning


class DefaultVersioning(URLPathVersioning):
    # default_version = ...
    # allowed_versions = ...
    # version_param = ...

    versioning_class = versioning.QueryParameterVersioning
