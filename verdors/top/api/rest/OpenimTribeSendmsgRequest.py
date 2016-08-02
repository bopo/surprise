'''
Created by auto_sdk on 2016.03.29
'''
from top.api.base import RestApi


class OpenimTribeSendmsgRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.msg = None
        self.tribe_id = None
        self.user = None

    def getapiname(self):
        return 'taobao.openim.tribe.sendmsg'
