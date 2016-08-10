# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase


class SearchTest(APITestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_list(self):
        response = self.client.get('/api/v1.0/search/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_with_category(self):
        response = self.client.get('/api/v1.0/search/?category=1', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/v1.0/search/?category=2', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/v1.0/search/?category=90', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_with_detail(self):
    #     response = self.client.get('/api/v1.0/search/AAEgvuLyACLm9G8Glr2jE20j/', format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
