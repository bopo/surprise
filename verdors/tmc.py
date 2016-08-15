# -*- coding: utf-8 -*-
import top.api

appkey = '23255563'
secret = 'f7092fdb96f20625742d577820936b5c'

req = top.api.TmcMessagesConsumeRequest()
req.set_app_info(top.appinfo(appkey,secret))
 
# req.group_name="vip_user"
req.quantity = 100

try:
    resp = req.getResponse()
    print(resp)
except Exception, e:
    print(e)