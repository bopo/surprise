# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase


class WatchwordTest(APITestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # def test_get_list(self):
    #     response = self.client.get('/api/v1.0/watchword/', format='json')
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
    #
    # def test_create(self):
    #     data = {
    #         "watchword": r"复制整段信息，打开👉天猫APP👈，即可查看此商品:【Xiaomi/小米 小米蓝牙音箱 插卡便携车载迷你无线蓝牙音响低音炮】。(未安装App点这里：http://share.laiwang.com/s/63ewr?tm=8db4c7 )🔑喵口令🔑",
    #         "sort": 'null'
    #     }
    #
    #     response = self.client.post('/api/v1.0/watchword/', data=data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
