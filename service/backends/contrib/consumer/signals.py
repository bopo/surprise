# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch import Signal, receiver

from restful.models.affairs import Notice

register_prepared = Signal(providing_args=["class"])
pre_register = Signal(providing_args=["class"])
post_register = Signal(providing_args=["class"])
post_follow = Signal(providing_args=["class"])
post_subscribe = Signal(providing_args=["class"])
post_like = Signal(providing_args=["class"])
post_favorite = Signal(providing_args=["class"])


# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from restful.tasks import do_push_work

@receiver(post_save, sender=Notice)
def signal_receiver(sender, **kwargs):
    pass

# @receiver(post_save, sender=Notice)
# def sync_jpush(instance, created, **kwargs):
#     if created:
#         uid = None
#         if instance.owner:
#             uid = instance.owner.pk
#
#         do_push_work(msgs=instance.title, uid=uid)
#
#         print "sync_push."
