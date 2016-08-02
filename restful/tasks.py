# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import time

import jpush as jpush
import requests
from celery.task import task
from django.conf import settings
from django.db.models import Q
from django.utils.timezone import now, timedelta
from dynamic_scraper.utils.task_utils import TaskUtils

from restful.models.reward import Reward
from restful.models.scraper import CollectWebsite, Goods
from restful.models.trade import Trade


@task()
def run_spiders():
    t = TaskUtils()
    t.run_spiders(CollectWebsite, 'scraper', 'scraper_runtime', 'goods_spider')


@task()
def run_checkers():
    t = TaskUtils()
    t.run_checkers(Goods, 'collect_website__scraper', 'checker_runtime', 'goods_checker')


@task
def _do_kground_work(name):
    """
    这里用time 模拟耗时操作
    """
    for i in range(1, 10):
        print 'hello:%s %s' % (name, i)

    time.sleep(1)


def get_data():
    url = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT' \
          '&cmd=0000011,3990012,3990052,3990062,hsi5,djia7&sty=MPNSBAS&st=&sr=1' \
          '&p=1&ps=1000&token=44c9d251add88e27b65ed86506f6e5da' \
          '&cb=callback08571712439879775&callback=callback08571712439879775&_=1457324522778'

    req = requests.get(url)
    txt = req.text.replace('callback08571712439879775', '').strip('(').strip(')')
    ret = json.loads(txt)

    return ret[0].split(',')[3]


def do_push_work(msgs=None, uid=None, *args, **kwargs):
    opts = jpush.JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
    push = opts.create_push()

    extras = {'uid': uid} and uid

    push.notification = jpush.notification(alert=msgs)

    push.options = {"time_to_live": 86400, 'sendno': 12345, "apns_production": True, 'extras': extras}
    # push.message = msgs

    push.audience = jpush.all_
    push.platform = jpush.all_

    push.send()


@task
def do_reward_work():
    value = get_data()

    if value:
        value = value.replace('.', '')
        value = value[-3:]
        today = now().date()

        yestoday = today - timedelta(days=1)

        print today, yestoday

        t = Reward.objects.get_or_create(today=today, value=value)
        t = Trade.objects.filter(Q(created__lt=today) & Q(number__startswith=value[:1]) & Q(rebate__isnull=True))

        if t:
            for x in t:
                x.reward = 1
                x.rebate = '0.9'
                x.save()
                # push_msg()

        t = Trade.objects.filter(Q(created__lt=today) & Q(number__startswith=value[:2]) & Q(rebate__isnull=True))

        if t:
            for x in t:
                x.reward = 1
                x.rebate = '0.5'
                x.save()
                # push_msg()

        t = Trade.objects.filter(Q(created__lt=today) & Q(number=value) & Q(rebate__isnull=True))

        if t:
            for x in t:
                x.reward = 1
                x.rebate = '1.0'
                x.save()
                # push_msg()

        print '[-] Updated today value is %s' % value
    else:
        print '[!] error!'
