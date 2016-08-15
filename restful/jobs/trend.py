# -*- coding: utf-8 -*-
from colorama import Fore
from django.utils.timezone import now
from django_extensions.management.jobs import BaseJob

from restful.lottery import has_exchange
from restful.models.total import Trend
from restful.utils import get_trend


class Job(BaseJob):
    help = "My trend job."

    def execute(self):
        try:
            if has_exchange(today=now().date()):
                object, status = Trend.objects.get_or_create(exchange=now(), number=get_trend())

                if status:
                    print Fore.GREEN + '[√] update data success!', object
                else:
                    print Fore.RED + '[*] igonre data!', object
            else:
                print Fore.RED + '[!!]', '今天是休息日,不能开奖'
        except Exception, e:
            raise e
