# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0043_auto_20160623_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prompt',
            old_name='switchs',
            new_name='switch2',
        ),
    ]
