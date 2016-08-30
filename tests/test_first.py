# -*- coding: utf-8 -*-
import json
import random

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from restful.contrib.consumer.models import CustomUser
from restful.models.goods import Goods
from restful.models.reward import FirstPrize, SCREENSIZE_CHOICES


class FirstTest(APITestCase):
    def setUp(self):
        self.user = self.create_user('lauren')
        self.user.set_password('secret')

        items = open('tests/goods.json').read()
        items = json.loads(items)

        platform = 'android'

        self.items = items

        # 构建商品数据
        for item in items:
            _ = Goods.objects.get_or_create(title=item.get('title'), open_iid=item.get('open_iid'),
                price=item.get('price'), pic_url=item.get('pic_url'), commission_rate=500.00)

        # index = [random.randint(0, len(items)) for _ in range(len(items))]

        # 构建赠品数据
        for i in SCREENSIZE_CHOICES:
            platform = 'ios' if platform == 'android' else 'android'
            _ = FirstPrize.objects.create(platform='ios', screensize=i[0],
                prizegoods=items[random.randint(0, len(items) - 1)].get('open_iid'))

        _ = FirstPrize.objects.create(platform='android', phonemodel='MI4L', phonebrand='MI',
            prizegoods=items[random.randint(0, len(items) - 1)].get('open_iid'))

        _ = FirstPrize.objects.create(platform='android',
            prizegoods=items[random.randint(0, len(items) - 1)].get('open_iid'))

        _ = FirstPrize.objects.create(platform='ios',
            prizegoods=items[random.randint(0, len(items) - 1)].get('open_iid'))

        # 认证系统
        token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def tearDown(self):
        pass

    def test_ios(self):
        data = {
            "platform": 'ios',
            "coordinate": "110.23432,220.23423",
            "screensize": "320x480",
            "phonebrand": "",
            "phonemodel": "",
        }

        # 认证系统
        token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/api/v1.0/first/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_android(self):
        data = {
            "platform": 'android',
            "coordinate": "110.23432,220.23423",
            "phonebrand": "MI4",
            "phonemodel": "MI4L",
        }
        print data
        # 认证系统
        token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/api/v1.0/first/', data=data, format='json')

        print response.content
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_others(self):
        data = {
            "platform": 'android',
            "coordinate": "110.23432,220.23423",
        }

        # 认证系统
        token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.post('/api/v1.0/first/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, msg=response.content)

        data = {
            "platform": 'ios',
            "coordinate": "110.2343232,220.123123",
        }

        # 认证系统
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/api/v1.0/first/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, msg=response.content)

    def create_user(self, username):
        return CustomUser.objects.create(username=username)
