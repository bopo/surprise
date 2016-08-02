'''
Created by auto_sdk on 2015.12.25
'''
from top.api.base import RestApi


class OpenSmsSendmsgRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.send_message_request = None

    def getapiname(self):
        return 'taobao.open.sms.sendmsg'
