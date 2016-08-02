# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase


class FeedbackTest(APITestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_list(self):
        response = self.client.get('/api/v1.0/feedback/', format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create(self):
        data = {
            "contact": "ibopo@126.com",
            "content": "你好,非常喜欢这个APP"
        }

        response = self.client.post('/api/v1.0/feedback/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
