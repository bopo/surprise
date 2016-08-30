# -*- coding: utf-8 -*-
import json

from faker import Faker
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from restful.contrib.consumer.models import CustomUser
from restful.models.affairs import Affairs
from restful.models.goods import Goods
from restful.models.trade import Trade


class TradeTest(APITestCase):
    today = None

    def setUp(self):
        self.user = self.create_user('lauren')
        self.user.set_password('secret')

        items = open('tests/goods.json').read()
        items = json.loads(items)

        self.items = items

        for item in items:
            Goods.objects.get_or_create(title=item.get('title'), open_iid=item.get('open_iid'), price=item.get('price'),
                pic_url=item.get('pic_url'), commission_rate=500.00, promotion_price=item.get('price'))

        token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def tearDown(self):
        pass

    def test_standard(self):
        f = Faker()
        g = Goods.objects.order_by('?')[1]

        orderid = f.credit_card_number()

        data = {
            "number": f.numerify(),
            "orderid": orderid,
            "open_iid": g.open_iid,
            "nums": 1,
            "price": g.price,
        }

        response = self.client.post('/api/v1.0/trade/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 判断订单信息
        orders = Trade.objects.get(orderid=orderid)
        self.assertTrue(orders)

        # 判断订单交易
        f = Faker()
        g = Goods.objects.order_by('?')[1]

        orderid = f.credit_card_number()

        data = {
            "number": f.numerify(),
            "orderid": orderid,
            "open_iid": g.open_iid,
            "rebate": "0.20",
            "price": g.promotion_price,
            "nums": 1,
        }

        response = self.client.post('/api/v1.0/trade/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # affairs = Affairs.objects.filter(orderid=orderid)
        orders = Trade.objects.filter(orderid=orderid)

        self.assertTrue(orders)
        # self.assertEqual('in', affairs.pay_type)
        # self.assertEqual(round(float(g.price) * float(data['rebate']), 2), float(affairs.payment))
        # self.assertEqual(orders.get().reward, 2)

    def create_user(self, username):
        return CustomUser.objects.create(username=username)
