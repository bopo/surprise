# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0033_auto_20160602_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='item_imgs',
            new_name='item_img',
        ),
    ]
