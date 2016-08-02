'''
Created by auto_sdk on 2015.12.14
'''
from top.api.base import RestApi


class BaichuanMessageSendNotificationRequest(RestApi):
    def __init__(self, domain='gw.api.taobao.com', port=80):
        RestApi.__init__(self, domain, port)
        self.channel = None
        self.content_text = None
        self.extra_map = None
        self.large_icon = None
        self.message_desc = None
        self.mobile_number = None
        self.open_type = None
        self.open_url = None
        self.save_timeout = None
        self.sms_context = None
        self.sms_delay_time = None
        self.sms_signature_id = None
        self.sms_template_id = None
        self.summary = None
        self.target_device_token = None
        self.title = None

    def getapiname(self):
        return 'taobao.baichuan.message.sendNotification'
