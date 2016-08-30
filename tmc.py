# -*- coding: utf-8 -*-
import json
import time

import top.api

APPKEY = '23255563'
SECRET = 'f7092fdb96f20625742d577820936b5c'


def main():
    req = top.api.TmcMessagesConsumeRequest()
    req.set_app_info(top.appinfo(APPKEY, SECRET))

    try:
        resp = req.getResponse()
        resp = json.dumps(resp)

        fp = open('tmc.log','a')
        fp.write(resp)
        fp.close()

        print resp
    except Exception, e:
        print(e)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(5)
