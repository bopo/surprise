#!/bin/bash

PGPASSWORD="secret" /usr/bin/pg_dump -U surprise surprise > /home/apps/dbs/surprise/$(date +%Y-%m-%d_%H:%M).backup
# /root/.virtualenvs/surprise/bin/python /home/apps/surprise/manage.py dumpdata --format=json > /home/apps/surprise/database/backups/$(date +%Y-%m-%d_%H:%M).json