# -*- coding: utf-8 -*-
from datetime import timedelta

from django.test import TestCase
from django.utils.timezone import now

from restful.contrib.consumer.models import CustomUser
from restful.jobs.reward import reward
from restful.models.affairs import Affairs
from restful.models.total import Trend
from restful.models.trade import Trade


class RewardTest(TestCase):
    today = None

    def setUp(self):
        # 初始化一些订单数据
        res1 = self.create_user('foo@example.com')
        res2 = self.create_user('bar@example.com')
        res3 = self.create_user('baz@example.com')
        self.today = now().date() + timedelta(days=-3)
        print self.today

        Trade.objects.create(orderid=123, number=123, title='2015母爱感恩行：不忘初心，方得信赖1', exchange=self.today, owner=res1)
        Trade.objects.create(orderid=456, number=127, title='2015母爱感恩行：不忘初心，方得信赖2', exchange=self.today, owner=res2)
        Trade.objects.create(orderid=789, number=135, title='2015母爱感恩行：不忘初心，方得信赖3', exchange=self.today, owner=res3)
        Trade.objects.create(orderid=78900, number=135, title='2015母爱感恩行：不忘初心，方得信赖3', exchange=self.today, owner=res3)
        Trade.objects.create(orderid=7819, number=565, title='2015母爱感恩行：不忘初心，方得信赖3', exchange=self.today, owner=res3)
        Trade.objects.create(orderid=7839, number=342, title='2015母爱感恩行：不忘初心，方得信赖3', exchange=self.today, owner=res3)

        # 初始化一些股票数据
        Trend.objects.create(exchange=self.today, number='123')

        # f = Faker()

        # for i in range(10):
        #     Trend.objects.create(exchange=self.today + timedelta(days=-i), number=f.numerify())

    def tearDown(self):
        pass

    def test_hits(self):
        result = reward(self.today)
        self.assertIsNotNone(result)

        for instance in result:
            affairs = Affairs.objects.get(orderid=instance['orderid'])
            orders = Trade.objects.get(orderid=instance['orderid'])

            self.assertTrue(affairs)
            self.assertEqual('in', affairs.pay_type)
            self.assertEqual(round(float(instance['price']) * float(instance['rebate']), 2), float(affairs.payment))
            self.assertEqual(orders.reward, 1)

    def create_user(self, username):
        return CustomUser.objects.create(username=username)
