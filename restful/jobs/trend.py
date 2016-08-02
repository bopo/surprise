# -*- coding: utf-8 -*-
from django.utils.timezone import now
from django_extensions.management.jobs import BaseJob

from restful.models.total import Trend
from restful.utils import get_trend


class Job(BaseJob):
    help = "My sample job."

    def execute(self):
        try:
            if now().isoweekday() <= 5:
                Trend.objects.create(exchange=now(), number=get_trend())
                print 'update data success!'
            else:
                print 'isoweekday =', now().isoweekday()
        except Exception, e:
            raise e
