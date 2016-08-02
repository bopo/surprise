'''
Created by auto_sdk on 2015.12.09
'''
from top.api.base import RestApi


class BaichuanMessageSendMessageRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.channel = None
        self.extra_map = None
        self.message = None
        self.message_desc = None
        self.save_timeout = None
        self.target_device_token = None

    def getapiname(self):
        return 'taobao.baichuan.message.sendMessage'
