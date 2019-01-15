# -*- coding: utf-8 -*-

import jpush
from django.conf import settings
from jinja2 import Template

from restful.models.affairs import NoticeTemplate


def pushMessage(messages=None, extra=None, *args, **kwargs):
    template = Template(messages)
    messages = template.render(dict(*args, **kwargs))

    push = jpush.JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
    push = push.create_push()

    push.notification = jpush.notification(alert=messages, ios=messages, android=messages)
    push.options = {"time_to_live": 86400, "sendno": 12345, "apns_production": False}
    push.platform = jpush.platform("ios", "android")
    push.send()

    return True


# 13165ffa4e0e1452159
# signup
class Notification:
    category = None

    def __init__(self, category=None):
        self.category = category

    def send(self, *args, **kwargs):

        try:
            content = NoticeTemplate.objects.get(category=self.category)
        except NoticeTemplate.DoesNotExist:
            print u"没有发现模板"
            return False

        print content.content

        template = Template(content.content)
        messages = template.render(dict(*args, **kwargs))

        registration_id = kwargs.get('registration_id')

        opts = jpush.JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
        push = opts.create_push()

        push.notification = jpush.notification(alert=messages)
        push.options = {"time_to_live": 86400, "apns_production": True, 'extras': kwargs.get('extras')}
        push.audience = jpush.audience(jpush.registration_id(registration_id)) if registration_id else jpush.all_
        push.platform = jpush.all_
        push.send()


def do_push_msgs(msgs=None, mobile=None, registration_id=None, *args, **kwargs):
    opts = jpush.JPush(settings.JPUSH_APPKEY, settings.JPUSH_SECRET)
    push = opts.create_push()

    extras = {'mobile': mobile}

    push.notification = jpush.notification(alert=msgs)
    push.options = {"time_to_live": 86400, "apns_production": True, 'extras': extras}
    push.audience = jpush.audience(jpush.registration_id(registration_id)) if registration_id else jpush.all_
    push.platform = jpush.all_
    push.send()

    return True
