from __future__ import absolute_import

from celery import shared_task
from django.core.mail import send_mail

from restful.message import Notification


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def do_push_notification(*args, **kwargs):
    data = dict(*args, **kwargs)
    Notification(data.get('category')).send(data)


@shared_task
def do_send_email(*args, **kwargs):
    data = dict(*args, **kwargs)
    vars = locals()

    for k, v in data.items():
        vars[k] = v

    send_mail(locals())


@shared_task
def do_send_sms(*args, **kwargs):
    data = dict(*args, **kwargs)
    pass
