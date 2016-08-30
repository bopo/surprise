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
            tmcs = resp['tmc_messages_consume_response']['messages']

            if tmcs:

                for tmc in tmcs['tmc_message']:
                    content = json.loads(tmc['content'])
                    orderid = content['order_id']
                    mesgsid = str(tmc['id'])

                    status = content['order_status']
                    extra = content.get('extre')

                    ret = Trade.objects.filter(orderid=orderid).update(
                        order_status=status,
                        confirmed=now(),
                        extra=extra
                    )

                    print mesgsid, ret

                    self.confirmed(mesgsid)

        except TopException, e:
            print(e)

    def confirmed(self, mesgsid):
        '''
        {
            "tmc_messages_confirm_response":{
            "is_success":true
            }
        }
        '''

        if not mesgsid:
            return None

        req = top.api.TmcMessagesConfirmRequest()
        req.set_app_info(top.appinfo(APPKEY, SECRET))
        req.s_message_ids = ",".join(mesgsid)

        try:
            resp = req.getResponse()
            tmcs = resp.get('tmc_messages_confirm_response')

            if tmcs.get('is_success'):
                print 'ok'

            print resp

        except TopException, e:
            print(e)
