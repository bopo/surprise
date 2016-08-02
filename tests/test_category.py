# -*- coding: utf-8 -*-

from rest_framework import status
from rest_framework.test import APITestCase

from restful.models.goods import GoodsCategory as Category


class CategoryTest(APITestCase):
    def setUp(self):
        category = Category.objects.create(name='test')

    def tearDown(self):
        pass

    def test_get_list(self):
        response = self.client.get('/api/v1.0/category/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_children(self):
        response = self.client.get('/api/v1.0/category/1/children/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
