# -*- coding: utf-8 -*-
from datetime import timedelta

from django.utils.timezone import now

from .models.affairs import Holiday
from .models.prompt import Prompt
from .models.trade import Trade


def get_exchange():
    # instance = Prompt.objects.first()
    # switch__ = instance.switchs if instance else False
    holiday = Holiday.objects.filter(year=now().year)

    total = 1
    today = now().date()

    # if switch__:
    #     total = Trade.objects.filter(owner=user, created__exact=now()).count()
    #     total = int(total) + 1

    while True:
        if not holiday:
            break

        forward = now().date() + timedelta(days=+total)

        if str(forward) not in holiday.get().date.split(','):
            break

        total -= 1

    # 周六日休市
    weeks = today.isoweekday()
    total = weeks - 5 if weeks > 5 else total
    return today + timedelta(days=-total)


def has_exchange(today):
    holiday = Holiday.objects.filter(year=now().year)
    today = now().date() if not today else today
    weeks = today.isoweekday()

    if holiday:
        if str(today) in holiday.get().date.split(','):
            return False

    # 周六日休市
    return False if weeks > 5 else True


def set_exchange(user):
    instance = Prompt.objects.first()
    switch__ = instance.switchs if instance else False

    holiday = Holiday.objects.filter(year=now().year)

    total = 1
    today = now().date()

    if switch__:
        total = Trade.objects.filter(owner=user, created__exact=now()).count()
        total = int(total) + 1

    while True:
        if not holiday:
            break

        forward = today + timedelta(days=+total)

        if str(forward) not in holiday.get().date.split(','):
            break

        total += 1

    # 周六日休市
    weeks = today.isoweekday()
    total += weeks - 5 if weeks > 5 else 0

    return today + timedelta(days=+total)
