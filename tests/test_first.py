# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase


class FirstTest(APITestCase):
    def setUp(self):
        # @todo 写入奖品
        pass

    def tearDown(self):
        pass

    # def test_get_list(self):
    #     response = self.client.get('/api/v1.0/first/', format='json')
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    #
    # def test_create(self):
    #     data = {
    #         "platform": 'ios',
    #         "coordinate": "110,220",
    #         "screensize": "480x320"
    #     }
    #
    #     response = self.client.post('/api/v1.0/first/', data=data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
