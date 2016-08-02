# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase


class StartTest(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/v1.0/start/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        del response

        response = self.client.get('/api/v1.0/start', format='json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        del response

    def test_get_detail(self):
        response = self.client.get('/api/v1.0/start/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/v1.0/start', format='json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_post(self):
        response = self.client.get('/api/v1.0/start/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/v1.0/start', format='json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_put(self):
        response = self.client.get('/api/v1.0/start/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/v1.0/start', format='json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_delete(self):
        response = self.client.get('/api/v1.0/start/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/v1.0/start', format='json')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

        # /api/v1.0/first/
        # /api/v1.0/trade/
        # /api/v1.0/bests/
        # /api/v1.0/query/
        # /api/v1.0/search/
        # /api/v1.0/category/
        # /api/v1.0/feedback/
        # /api/v1.0/location/
        # /api/v1.0/recommend/
        # /api/v1.0/watchword/
