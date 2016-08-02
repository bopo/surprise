'''
Created by auto_sdk on 2015.12.17
'''
from top.api.base import RestApi


class OpenSmsBatchsendmsgRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.params = None

    def getapiname(self):
        return 'taobao.open.sms.batchsendmsg'
