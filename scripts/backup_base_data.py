# -*- coding: utf-8 -*-
import os

import sys
import time

FIXTURES = (
    'flatpages',
    'restful.goodscategory',
    'restful.total',
    'restful.goods',
    'restful.prompt',
    'restful.banner',
    'restful.holiday',
    'restful.queryrule',
    'consumer.customuser',
)


def local(cmd):
    # os.system(cmd)
    print cmd
    pass


def run():
    backdir = 'database/backups/%s' % time.strftime('%Y%m%d%H', time.localtime())

    if not os.path.isdir(backdir):
        os.makedirs(backdir)

    for num, fixture in enumerate(FIXTURES):
        local('source $VIRTUALENVWRAPPER_SCRIPT && workon server && ptyhon manage.py dumpdata {} > {}/00{}_{}.json'.format(fixture, backdir, num + 1, fixture))
