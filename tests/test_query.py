# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase


class QueryTest(APITestCase):
    def setUp(self):
        # @todo 写入奖品
        pass

    def tearDown(self):
        pass

    def test_get_list(self):
        response = self.client.get('/api/v1.0/query/', format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # def test_get_keyword(self):
    #     data = {
    #         "keyword": "女鞋",
    #         "page_no": None,
    #         "page_size": None,
    #         "sort": ""
    #     }
    #
    #     response = self.client.get('/api/v1.0/query/', data=data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
