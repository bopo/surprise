# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0024_goodscategory_cid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taobaocategory',
            name='cid',
        ),
    ]
