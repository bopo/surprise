# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase


class LocationTest(APITestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_list(self):
        response = self.client.get('/api/v1.0/location/', format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create(self):
        data = {
            "address": "1111",
            "coordinate": "23232,2323",
            "imei": "23423423"
        }

        response = self.client.post('/api/v1.0/location/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
