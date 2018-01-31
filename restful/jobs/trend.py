# -*- coding: utf-8 -*-
from django.utils.timezone import now
from django_extensions.management.jobs import BaseJob
from fabric.colors import green, red

from restful.lottery import has_exchange
from restful.models.total import Trend, Total
from restful.utils import get_trend


class Job(BaseJob):
    help = "My trend job."

    def execute(self):
        try:
            today = now().date()
            if has_exchange(today=today):
                object, status = Trend.objects.get_or_create(exchange=now().date())

                if status:
                    object.number = get_trend()
                    object.save()

                    total = Total.objects.last()
                    total.number = object.number
                    total.exchange=now()
                    total.save()

                    print green('[√] update data success!'), object
                else:
                    print red('[*] igonre data!'), object
            else:
                print red('[!!] 今天是休息日,不能开奖')
        except Exception, e:
            raise e
