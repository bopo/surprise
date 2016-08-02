#!/usr/bin/env python
import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), 'verdors'))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.tests'
    django.setup()

    Test_Runner = get_runner(settings)
    test_runner = Test_Runner()

    failures = test_runner.run_tests(["tests"])

    sys.exit(bool(failures))
