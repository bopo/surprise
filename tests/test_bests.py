# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase


class BestsTest(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/v1.0/bests/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        del response
