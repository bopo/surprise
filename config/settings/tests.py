# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os,sys
# COVERAGE_MODULES = ['restful']
# TEST_RUNNER = 'config.testrunner.test_runner_with_coverage'
sys.path.append(os.path.join(os.path.dirname(__file__), '../../verdors'))

try:
    from .base import *
except ImportError, e:
    raise e

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '..', 'database', 'db.sqlite3'),
    },
}

TEST_DEBUG = True
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# Test runner
# TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'
# TEST_RUNNER = 'django_coverage.coverage_runner.CoverageRunner'
