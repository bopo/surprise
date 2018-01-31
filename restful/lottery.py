# -*- coding: utf-8 -*-

from django.utils.timezone import now, timedelta

from restful.models.affairs import Holiday

HOLIDAY = Holiday.objects.filter(year=now().year).get().date.split(',')


def get_exchange(today=None):
    # instance = Prompt.objects.first()
    # switch__ = instance.switchs if instance else False
    # holiday = Holiday.objects.filter(year=now().year)

    total = 1
    today = now().date() if today is None else today

    # if switch__:
    #     total = Trade.objects.filter(owner=user, created__exact=now()).count()
    #     total = int(total) + 1

    # 周六日休市
    weeks = today.isoweekday()
    total = weeks - 5 if weeks > 5 else total
    total = weeks + 2 if weeks == 1 else total

    # 判断是否节假日
    while True:
        if not HOLIDAY:
            break

        forward = today + timedelta(days=-total)

        # 判断不是休市
        if str(forward) not in HOLIDAY:
            # 判断周末
            weeks = forward.isoweekday()
            total = weeks - 5 if weeks > 5 else total
            break

        total += 1
    print today + timedelta(days=+total)
    return today + timedelta(days=-total)


def has_exchange(today):
    today = now().date() if not today else today
    weeks = today.isoweekday()

    if HOLIDAY:
        if str(today) in HOLIDAY:
            return False

    # 周六日休市
    return False if weeks > 5 else True


def set_exchange(user=None, today=None):
    # instance = Prompt.objects.first()
    # switch__ = instance.switchs if instance else False

    # holiday = Holiday.objects.filter(year=now().year)

    total = 1
    today = now().date() if today is None else today

    # if switch__:
    #     total = Trade.objects.filter(owner=user, created__exact=now()).count()
    #     total = int(total) + 1

    # 周六日休市
    # weeks = today.isoweekday()
    # total += weeks - 5 if weeks > 5 else 0
    weeks = today.isoweekday()
    total = 8 - weeks if weeks >= 5 else total

    while True:
        if not HOLIDAY:
            break

        forward = today + timedelta(days=+total)
        weeks = forward.isoweekday()
        total += 8 - weeks if weeks >= 5 else 0
        forward = today + timedelta(days=+total)

        # 判断非休市
        if str(forward) not in HOLIDAY:
            # 判断周末
            # print str(forward.date())

            break

        total += 1

    return today + timedelta(days=+total)
