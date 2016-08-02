#  -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'verdors'))

from .pub_base import *

CHANNEL = 'qqhd'


def run():
    navs(channel=CHANNEL)
    # main(channel=CHANNEL, pages=1, cats=90, syncdb=False)
