# -*- coding: utf-8 -*-
import json

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from restful.contrib.consumer.models import CustomUser
from restful.models.goods import Goods
from restful.models.reward import FirstPrize


class FirstTest(APITestCase):
    def setUp(self):
        self.user = self.create_user('lauren')
        self.user.set_password('secret')

        items = open('tests/goods.json').read()
        items = json.loads(items)

        platform = 'android'

        self.items = items

        for item in items:
            platform = 'ios' if platform == 'android' else 'android'
            _ = Goods.objects.get_or_create(title=item.get('title'), open_iid=item.get('open_iid'),
                price=item.get('price'), pic_url=item.get('pic_url'), commission_rate=500.00)

            _ = FirstPrize.objects.create(platform='ios', screensize='320x480', prizegoods=item.get('open_iid'))

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

        token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/api/v1.0/first/', data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_android(self):
        data = {
            "platform": 'android',
            "coordinate": "110.23432,220.23423",
            "phonebrand": "MI4",
            "phonemodel": "",
        }

        token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post('/api/v1.0/first/', data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def create_user(self, username):
        return CustomUser.objects.create(username=username)
