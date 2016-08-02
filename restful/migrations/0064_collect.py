# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0063_remove_goods_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default='draft', max_length=100, verbose_name='status', no_check_for_status=True, choices=[('draft', 'draft'), ('published', 'published')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('price', models.DecimalField(null=True, verbose_name='\u4ef7\u683c', max_digits=10, decimal_places=2, blank=True)),
                ('promotion_price', models.CharField(max_length=255, null=True, verbose_name='\u4fc3\u9500\u4ef7\u683c', blank=True)),
                ('pic_url', models.URLField(max_length=255, null=True, verbose_name='\u56fe\u7247url', blank=True)),
                ('num_iid', models.BigIntegerField(null=True, verbose_name='\u5546\u54c1\u771fid', blank=True)),
                ('category', models.ForeignKey(verbose_name='\u5546\u54c1\u5206\u7c7b', to='restful.GoodsCategory', null=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': '\u91c7\u96c6\u4e34\u65f6\u5e93',
                'verbose_name_plural': '\u91c7\u96c6\u4e34\u65f6\u5e93',
            },
        ),
    ]
