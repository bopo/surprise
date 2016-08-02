# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase


class RecommendTest(APITestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_list(self):
        response = self.client.get('/api/v1.0/recommend/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_with_category(self):
        response = self.client.get('/api/v1.0/recommend/?category=1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/v1.0/recommend/?category=2', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/v1.0/recommend/?category=90', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
