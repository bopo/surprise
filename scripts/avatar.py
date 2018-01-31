# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from restful.contrib.consumer.models import CustomUser, UserProfile


def run():
    for x in open('scripts/username.txt'):
        u = x.strip()
        name, avatar = u.split('|')
        name = name.strip()
        avatar = avatar.strip()
        c, _ = CustomUser.objects.get_or_create(username=name)
        p, _ = UserProfile.objects.get_or_create(owner=c)
        p.avatar = avatar
        p.name = name
        p.save()

        print name, avatar
