# -*- coding: utf-8 -*-

from rest_framework.test import APITestCase

from restful.contrib.consumer.models import CustomUser


class TmcTest(APITestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ios(self):
        pass

    def create_user(self, username):
        return CustomUser.objects.create(username=username)
