# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from .base import INSTALLED_APPS

INSTALLED_APPS += ('haystack',)

HAYSTACK_CONNECTIONS = {
    'solr': {
        # For Solr:
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://localhost:9001/solr/example',
        'TIMEOUT': 60 * 5,
        'INCLUDE_SPELLING': True,
    },
    'default': {
        # For Whoosh:
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
        'INCLUDE_SPELLING': True,
    },
    'simple': {
        # For Simple:
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
    'xapian': {
        # For Xapian (requires the third-party install):
        'ENGINE': 'xapian_haystack.xapian_backend.XapianEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'xapian_index'),
    }
}
