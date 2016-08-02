'''
Created by auto_sdk on 2015.03.23
'''
from top.api.base import RestApi


class IselectTaeItempoolSearchRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.numwords = None
        self.order = None
        self.pagenum = None
        self.pagesize = None
        self.qwords = None

    def getapiname(self):
        return 'taobao.iselect.tae.itempool.search'
