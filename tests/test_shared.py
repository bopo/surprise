# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils.timezone import timedelta, now

from restful.models.shared import shared_rule, Shared, SharedRule

today = now().date()


class SharedTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user('lauren')
        self.user.set_password('secret')

        start_date = today+ timedelta(days=-7)
        end_date = today + timedelta(days=7)

        # 初始化分享规则
        SharedRule.objects.create(every='day', number=2, price=0.5)
        SharedRule.objects.create(every='weekly', number=2, price=0.6)
        SharedRule.objects.create(every='monthly', number=2, price=0.7)
        SharedRule.objects.create(start_date=start_date, end_date=end_date, number=2, price=0.8)

    def tearDown(self):
        pass

    def init_data(self, start_date=today, days=1):
        for x in range(1, days):
            created = start_date + timedelta(days=-x)
            Shared.objects.create(owner=self.user, created=created, model='1')
            Shared.objects.create(owner=self.user, created=created, model='2')
            Shared.objects.create(owner=self.user, created=created, model='3')

    def flush_data(self):
        Shared.objects.all().delete()

    # def test_none(self):
    #     self.flush_data()
    #     ret = shared_rule(owner=self.user)
    #     self.assertFalse(ret)

    # 每天
    def test_every_day(self):
        rule = SharedRule.objects.get(every='day')
        self.init_data(start_date=today, days=1)
        every, nums, price = shared_rule(owner=self.user, today=today, rule=rule)

        print every, nums, price

        self.assertTrue(bool(rule))
        self.assertEqual(every, 'day')
        self.assertEqual(nums, 1)
        self.assertEqual(price, 0.5)
        self.flush_data()

    # 每周
    def test_every_week(self):
        rule = SharedRule.objects.get(every='weekly')
        self.init_data(start_date=today, days=1)
        every, nums, price = shared_rule(owner=self.user, today=today, rule=rule)

        self.assertEqual(every, 'weekly')
        self.assertEqual(nums, 1)
        self.assertEqual(price, 0.5)
        self.flush_data()
    #
    #     self.init_data(start_date=today, days=3)
    #     every, nums, price = shared_rule(owner=self.user, today=today, rule=rule)
    #     self.assertEqual(nums, 2)
    #     self.flush_data()
    #
    #     self.init_data(start_date=today, days=3)
    #     every, nums, price = shared_rule(owner=self.user, today=today, rule=rule)
    #     self.assertFalse(nums)
    #     self.assertFalse(price)
    #     self.assertFalse(every)
    #     self.flush_data()
    #
    # # 每月
    # def test_every_month(self):
    #     rule = SharedRule.objects.get(every='monthly')
    #     self.init_data(start_date=today, days=1)
    #     every, nums, price = shared_rule(owner=self.user, today=today, rule=rule)
    #
    #     self.assertEqual(every, 'weekly')
    #     self.assertEqual(nums, 1)
    #     self.assertEqual(price, 0.5)
    #     self.flush_data()
    #
    #     self.init_data(start_date=today, days=3)
    #     every, nums, price = shared_rule(owner=self.user, today=today, rule=rule)
    #     self.assertEqual(nums, 2)
    #     self.flush_data()
    #
    #     self.init_data(start_date=today, days=3)
    #     every, nums, price = shared_rule(owner=self.user, today=today, rule=rule)
    #     self.assertFalse(nums)
    #     self.assertFalse(price)
    #     self.assertFalse(every)
    #     self.flush_data()
    #
    # # 混合
    # def test_every_mixed(self):
    #     rule = SharedRule.objects.get(every='monthly')
    #     self.init_data(start_date=today, days=10)
    #     every, nums, price = shared_rule(owner=self.user, today=today, rule=rule)
    #
    #     self.assertEqual(every, 'weekly')
    #     self.assertEqual(nums, 1)
    #     self.assertEqual(price, 0.5)
    #
    #     rule = SharedRule.objects.get(every='weekly')
    #     every, nums, price = shared_rule(owner=self.user, today=today, rule=rule)
    #     self.assertEqual(nums, 2)
    #
    #     rule = SharedRule.objects.get(every='day')
    #     every, nums, price = shared_rule(owner=self.user, today=today, rule=rule)
    #     self.assertFalse(nums)
    #     self.assertFalse(price)
    #     self.assertFalse(every)
    #
    #     self.flush_data()
    #
    # # 时间周期
    # def test_expired(self):
    #     self.init_data(start_date=today, days=1)
    #     #
    #     self.init_data(start_date=today, days=1)
    #     #
    #
    # # 混合
    # def test_all_mixed(self):
    #     pass
