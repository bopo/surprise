#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    sys.path.append(os.path.join(os.path.dirname(__file__), 'verdors'))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    execute_from_command_line(sys.argv)
