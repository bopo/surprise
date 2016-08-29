# -*- coding: utf-8 -*-
import json

import top.api

APPKEY = '23255563'
SECRET = 'f7092fdb96f20625742d577820936b5c'

req = top.api.TmcMessagesConsumeRequest()
req.set_app_info(top.appinfo(APPKEY, SECRET))

try:
    resp = req.getResponse()
    resp['tmc_messages_consume_response']['messages']['tmc_message'] = json.loads(
        '{"buyer_id":"AAE8g3trABpL86adzOb7d948","extre":"","paid_fee":"0.02","order_id":"887450175487518","order_status":"2","auction_infos":[{"detail_order_id":"887450175497518","auction_id":"AAH3g3toABpL86adzOzgP5-G","auction_pict_url":"i1/TB1YZ_QGVXXXXcmXVXXXXXXXXXX_!!0-item_pic.jpg","auction_title":"0s-女装-发货合约8hrs-测试宝贝-拍下无效","auction_amount":"2"},{"detail_order_id":"887450175507518","auction_id":"AAH3g3toABpL86adzOzgP5-G","auction_pict_url":"i1/TB1YZ_QGVXXXXcmXVXXXXXXXXXX_!!0-item_pic.jpg","auction_title":"0s-女装-发货合约8hrs-测试宝贝-拍下无效","auction_amount":"2"}]}')
    resp = json.dumps(resp)
    print resp
except Exception, e:
    print(e)
