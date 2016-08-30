# -*- coding: utf-8 -*-
from django.db.models import Q
from django_extensions.management.jobs import BaseJob
from fabric.colors import red, green, blue, yellow
from jinja2 import Template
from model_utils.models import now

from ..lottery import has_exchange
from ..models.affairs import Notice, NoticeTemplate
from ..models.total import Trend
from ..models.trade import Trade


def reward(today):
    if not has_exchange(today):
        print red('[!!]', '今天是休息日,不能开奖')
        return False

    # 获取今天的股票大盘
    value = Trend.objects.filter(exchange=today)
    total = 0

    result = []

    if value:
        # 选择开奖日期是今天的订单
        orders = Trade.objects.filter(Q(exchange=today) & Q(rebate__isnull=True) & Q(confirmed__isnull=False) & (
        Q(order_status='2') | Q(order_status='6')))

        number = value.get().number

        if orders:
            for x in orders:
                # 全部相等
                if str(x.number)[:3] == str(number)[:3]:
                    x.reward = 1
                    x.rebate = '1.0'
                    x.save()
                    print blue('[√]' + x.owner.username), x.number, 1
                # '两位相等'
                elif str(x.number)[:2] == str(number)[:2]:
                    x.reward = 1
                    x.rebate = '0.5'
                    x.save()
                    print blue('[√]' + x.owner.username), x.number, 0.5
                # 一位相等
                elif str(x.number)[:1] == str(number)[:1]:
                    x.reward = 1
                    x.rebate = '0.1'
                    x.save()
                    print blue('[√]' + x.owner.username), x.number, 0.1
                else:
                    print yellow('[-]' + x.title + '   没有中奖')

                if x.reward == 1:
                    # 推送中奖消息
                    # self.push_lottery(x)

                    # 发送短信通知
                    # self.send_mobile(None)
                    result.append({'orderid': x.orderid, 'rebate': x.rebate, 'price': x.price})

                    total += 1

        else:
            print '没有订单'

        print green('[√] 今天的中奖人数 %s' % total)
    else:
        print red('[!!]', '现在还没有股票数据')

    return result


class Job(BaseJob):
    help = "My reward job."

    def execute(self):
        return reward(today=now().date())

        # if not has_exchange():
        #     print Fore.RED + '[!!]', '今天是休息日,不能开奖'
        #     return False
        #
        # today = now().date()
        # value = Trend.objects.filter(exchange=today)
        # total = 0
        #
        # if value:
        #     # 选择开奖日期是今天的订单
        #     orders = Trade.objects.filter(Q(exchange=today) & Q(rebate__isnull=True))
        #     number = value.get().number
        #
        #     for x in orders:
        #         if x.number[:3] == number[:3]:
        #             x.reward = 1
        #             x.rebate = '1.0'
        #             x.save()
        #         elif x.number[:2] == number[:2]:
        #             x.reward = 1
        #             x.rebate = '0.5'
        #             x.save()
        #         elif x.number[:1] == number[:1]:
        #             x.reward = 1
        #             x.rebate = '0.9'
        #             x.save()
        #
        #         if x.reward == 1:
        #             # 推送中奖消息
        #             self.push_lottery(x)
        #
        #             # 发送短信通知
        #             self.send_mobile(None)
        #
        #             total += 1
        #
        #     print Fore.GREEN + '[√] 今天的中奖人数 %s' % total
        # else:
        #     print Fore.RED + '[!!] error!'

    def push_lottery(self, obj):
        template = NoticeTemplate.objects.filter(slug='reward')
        template = Template(template)
        messages = template.render(dict(obj))

        title = ''

        notice = Notice.objects.create(title=title, content=messages, owner=obj.owner)
        notice.save()
        notice.push()

    def send_mobile(self, msg):
        print __name__
