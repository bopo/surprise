'''
Created by auto_sdk on 2014.10.11
'''
from top.api.base import RestApi


class AtbItemsDetailGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.fields = None
        self.open_iids = None

    def getapiname(self):
        return 'taobao.atb.items.detail.get'
