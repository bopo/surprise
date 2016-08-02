'''
Created by auto_sdk on 2015.07.09
'''
from top.api.base import RestApi


class UserBaichuanRecommendGetRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.id_type = None
        self.isv_app_id = None
        self.user_id = None

    def getapiname(self):
        return 'taobao.user.baichuan.recommend.get'
