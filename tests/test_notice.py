# -*- coding: utf-8 -*-
import json

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from restful.contrib.consumer.models import CustomUser
from restful.models.goods import Goods


class NoticeTest(APITestCase):
    def setUp(self):
        self.user = self.create_user('lauren')
        self.user.set_password('secret')

        # items = open('tests/goods.json').read()
        # items = json.loads(items)
        #
        # self.items = items
        #
        # for item in items:
        #     _ = Goods.objects.get_or_create(title=item.get('title'), open_iid=item.get('open_iid'),
        #         price=item.get('price'), pic_url=item.get('pic_url'), commission_rate=500.00)

    def tearDown(self):
        pass

    # def test_post_(self):
    #     data = {
    #         "platform": 'ios',
    #         "coordinate": "110.23432,220.23423",
    #         "screensize": "480x320",
    #         "phonebrand": "",
    #         "phonemodel": "",
    #     }
    #
    #     self.client.login(username='lauren', password='secret')
    #
    #     token, _ = Token.objects.get_or_create(user=self.user)
    #     self.assertIsNotNone(token)
    #
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    #     response = self.client.post('/api/v1.0/first/', data=data, format='json')
    #
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def create_user(self, username):
        return CustomUser.objects.create(username=username)
