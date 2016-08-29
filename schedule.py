#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#  Copyright © XYM
# Last modified: 2016-08-27 13:29:08

# -*- coding: utf-8 -*-

# Use this file to easily define all of your cron jobs.
#
# It's helpful to understand cron before proceeding.
# http://en.wikipedia.org/wiki/Cron
#
# Learn more: http://github.com/fengsp/plan

import click
from plan import Plan

cron = Plan("surprise", path='/home/apps/surprise', environment={'DJANGO_SETTINGS_MODULE': 'config.settings.prod'})
cron.script('manage.py runscript collect_liwushuo_items', every='9.hour')
# cron.script('manage.py runjob collect_nanyibang_items', every='9.hour')
# cron.script('manage.py runjob n2oid', every='3.hour')

cron.script('manage.py runjob tmc', every='5.minute')
cron.script('manage.py runjob trend', every='16.hour')
cron.script('manage.py runjob reward', every='1.day')

cron.command('/home/apps/surprise/crontab/db_backup.sh', every='15.minute')
cron.command('/usr/bin/rsync -av /home/apps/surprise /home/apps/backups', every='15.day')


@click.command()
@click.argument('action', default='check')
def execute(action):
    cron.run(action)


if __name__ == "__main__":
    execute()
