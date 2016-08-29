# -*- coding: utf-8 -*-
import json

from django.conf import settings
from django.utils.timezone import now
from django_extensions.management.jobs import BaseJob

import top.api
from restful.models.trade import Trade
from top.api.base import TopException

APPKEY = settings.TOP_APPKEY
SECRET = settings.TOP_SECRET


class Job(BaseJob):
    help = "My TMC job."

    def execute(self):

        req = top.api.TmcMessagesConsumeRequest()
        req.set_app_info(top.appinfo(APPKEY, SECRET))
        req.quantity = 100

        try:
            resp = req.getResponse()
            # 模拟数据
            # fp = open('tmc.json').read()
            # resp = json.loads(fp)
            tmcs = resp['tmc_messages_consume_response']['messages']
            # ---------------------------------
            fp = open('runtime/tmc/' + resp['tmc_messages_consume_response']['request_id'] + '.json', 'w')
            fp.write(json.dumps(resp))
            fp.close()
            # ---------------------------------

            # ---------------------------------
            if tmcs:
                # print tmcs['tmc_message']
                orderids = []
                mesgsids = []

                for tmc in tmcs['tmc_message']:
                    content = json.loads(tmc['content'])
                    orderid = content['order_id']
                    order_status = content['order_status']
                    orderids.append(orderid)
                    extra = content.get('extre')

                    mesgsids.append(str(tmc['id']))
                    print json.dumps(json.loads(tmc['content']))

                if len(orderids):
                    _ = Trade.objects.filter(orderid__in=orderids, confirmed__isnull=True).update(
                        confirmed=now(),
                        order_status=order_status,
                        extra=extra
                    )

                    print mesgsids, _
                    # 确认接口
                    self.confirmed(mesgsids)

                    # print resp

                    # 查询订单是否存在
                    # 更新订单确认
                    # 记录该次记录
        except TopException, e:
            print(e)

    def confirmed(self, mesgsids):
        '''
        {
            "tmc_messages_confirm_response":{
            "is_success":true
            }
        }
        '''

        # print ",".join(mesgsids)
        # return ",".join(mesgsids)

        req = top.api.TmcMessagesConfirmRequest()
        req.set_app_info(top.appinfo(APPKEY, SECRET))
        req.s_message_ids = ",".join(mesgsids)

        try:
            resp = req.getResponse()
            tmcs = resp.get('tmc_messages_confirm_response')

            if tmcs.get('is_success'):
                print 'ok'

            print resp

        except TopException, e:
            print(e)
