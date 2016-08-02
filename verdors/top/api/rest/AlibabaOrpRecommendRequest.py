'''
Created by auto_sdk on 2016.03.16
'''
from top.api.base import RestApi


class AlibabaOrpRecommendRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.appid = None
        self.call_source = None
        self.params = None
        self.userid = None

    def getapiname(self):
        return 'alibaba.orp.recommend'
