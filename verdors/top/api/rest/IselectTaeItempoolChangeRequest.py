'''
Created by auto_sdk on 2015.03.18
'''
from top.api.base import RestApi


class IselectTaeItempoolChangeRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.act = None
        self.open_iid = None

    def getapiname(self):
        return 'taobao.iselect.tae.itempool.change'
