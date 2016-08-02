# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_scraper', '__first__'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Affairs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', model_utils.fields.StatusField(default='ready', max_length=100, verbose_name='status', no_check_for_status=True, choices=[('ready', '\u672a\u63d0\u73b0'), ('done', '\u5df2\u63d0\u73b0')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('payment', models.DecimalField(default=0.0, verbose_name='\u53d1\u751f\u989d', max_digits=10, decimal_places=2)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u751f\u65f6\u95f4')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='\u64cd\u4f5c\u65f6\u95f4')),
                ('pay_type', models.CharField(default='in', max_length=20, verbose_name='\u6536\u652f\u7c7b\u578b', choices=[('in', '\u6536\u5165'), ('out', '\u652f\u51fa')])),
                ('owner', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('pk',),
                'verbose_name': '\u8d22\u52a1\u8bb0\u5f55',
                'verbose_name_plural': '\u8d22\u52a1\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.CharField(default='', max_length=100, verbose_name='\u63cf\u8ff0')),
                ('click', models.URLField(default='', verbose_name='\u7f51\u5740')),
                ('cover', models.ImageField(upload_to=b'', verbose_name='\u56fe\u7247', blank=True)),
                ('ordering', models.IntegerField(default='1', verbose_name='\u6392\u5e8f')),
            ],
            options={
                'ordering': ('pk',),
                'verbose_name': '\u6a2a\u5e45\u5e7f\u544a',
                'verbose_name_plural': '\u6a2a\u5e45\u5e7f\u544a',
            },
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u6e20\u9053\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u5b89\u88c5\u6e20\u9053',
                'verbose_name_plural': '\u5b89\u88c5\u6e20\u9053',
            },
        ),
        migrations.CreateModel(
            name='CollectWebsite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u540d\u79f0')),
                ('url', models.URLField()),
                ('scraper', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.Scraper', null=True)),
                ('scraper_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_price', models.DecimalField(default='0.00', verbose_name='\u6700\u5c0f\u4ef7\u683c', max_digits=10, decimal_places=2)),
                ('max_price', models.DecimalField(default='0.00', verbose_name='\u6700\u5927\u4ef7\u683c', max_digits=10, decimal_places=2)),
                ('discount', models.DecimalField(default='0.00', verbose_name='\u4e2d\u95f4\u6bd4\u7387', max_digits=10, decimal_places=2)),
            ],
            options={
                'verbose_name': '\u4e2d\u95f4\u6bd4\u7387',
                'verbose_name_plural': '\u4e2d\u95f4\u6bd4\u7387',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u4e8b\u4ef6\u53d1\u751f\u65f6\u95f4')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='First',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platform', models.CharField(default='android', max_length=50, verbose_name='APP\u5e73\u53f0', choices=[('ios', 'IOS'), ('android', 'Android')])),
                ('location', models.CharField(max_length=200, verbose_name='\u5730\u5740\u4fe1\u606f')),
                ('coordinate', models.CharField(max_length=200, verbose_name='\u4f4d\u7f6e\u5750\u6807')),
                ('screensize', models.CharField(max_length=200, verbose_name='\u5c4f\u5e55\u5c3a\u5bf8')),
                ('owner', models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u9996\u767b\u5956\u52b1',
                'verbose_name_plural': '\u9996\u767b\u5956\u52b1',
            },
        ),
        migrations.CreateModel(
            name='FirstPrize',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('platform', models.CharField(default='android', max_length=50, verbose_name='APP\u5e73\u53f0', choices=[('ios', 'IOS'), ('android', 'Android')])),
                ('location', models.CharField(max_length=200, verbose_name='\u5730\u5740\u4fe1\u606f')),
                ('coordinate', models.CharField(max_length=200, verbose_name='\u4f4d\u7f6e\u5750\u6807')),
                ('screensize', models.CharField(max_length=200, verbose_name='\u5c4f\u5e55\u5c3a\u5bf8', choices=[('1000', '\u5b98\u7f51'), ('1001', '91\u52a9\u624b'), ('1002', '\u767e\u5ea6'), ('1003', '\u5b89\u5353'), ('1004', '\u8c4c\u8c46\u835a'), ('1005', '\u5e94\u7528\u5b9d'), ('1006', '360'), ('1007', '\u5e94\u7528\u6c47'), ('1008', '\u9b45\u65cf'), ('1009', 'N\u591a\u7f51'), ('1010', 'PP\u52a9\u624b'), ('1011', '\u6dd8\u5b9d'), ('1012', '\u673a\u950b\u7f51'), ('1013', '\u91d1\u7acb'), ('1014', '\u5c0f\u7c73'), ('1015', '\u534e\u4e3a'), ('1016', '\u641c\u72d7'), ('1017', '\u5b89\u667a'), ('1018', '\u6c83\u5546\u5e97'), ('1019', 'itools'), ('1020', '\u7535\u4fe1\u7231\u6e38\u620f'), ('1021', '\u4f18\u4ebf\u5e02\u573a'), ('1022', '\u5e94\u7528\u8d1d'), ('1023', 'googleplay'), ('1024', '\u5b89\u7c89\u7f51')])),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default='draft', max_length=100, verbose_name='status', no_check_for_status=True, choices=[('draft', 'draft'), ('published', 'published')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('nick', models.CharField(max_length=100, null=True, verbose_name='\u5356\u5bb6\u6635\u79f0', blank=True)),
                ('seller_id', models.IntegerField(null=True, verbose_name='\u5356\u5bb6ID', blank=True)),
                ('item_location', models.CharField(max_length=100, null=True, verbose_name='\u5546\u54c1\u6240\u5728\u5730', blank=True)),
                ('seller_credit_score', models.IntegerField(null=True, verbose_name='\u5356\u5bb6\u4fe1\u7528\u7b49\u7ea7', blank=True)),
                ('commission', models.CharField(max_length=255, null=True, verbose_name='\u6dd8\u5b9d\u5ba2\u4f63\u91d1', blank=True)),
                ('commission_num', models.CharField(max_length=255, null=True, verbose_name='\u7d2f\u8ba1\u6210\u4ea4\u91cf', blank=True)),
                ('commission_rate', models.CharField(max_length=255, null=True, verbose_name='\u6dd8\u5b9d\u5ba2\u4f63\u91d1\u6bd4\u7387', blank=True)),
                ('commission_volume', models.CharField(max_length=255, null=True, verbose_name='\u7d2f\u8ba1\u603b\u652f\u51fa\u4f63\u91d1\u91cf', blank=True)),
                ('coupon_rate', models.DecimalField(null=True, verbose_name='\u6298\u6263\u6bd4\u7387', max_digits=10, decimal_places=2, blank=True)),
                ('coupon_price', models.DecimalField(null=True, verbose_name='\u6298\u6263\u4ef7\u683c', max_digits=10, decimal_places=2, blank=True)),
                ('coupon_start_time', models.DateTimeField(null=True, verbose_name='\u6298\u6263\u6d3b\u52a8\u5f00\u59cb\u65f6\u95f4', blank=True)),
                ('coupon_end_time', models.DateTimeField(null=True, verbose_name='\u6298\u6263\u6d3b\u52a8\u7ed3\u675f\u65f6\u95f4', blank=True)),
                ('promotion_price', models.CharField(max_length=255, null=True, verbose_name='\u4fc3\u9500\u4ef7\u683c', blank=True)),
                ('volume', models.CharField(max_length=255, null=True, verbose_name='30\u5929\u5185\u4ea4\u6613\u91cf', blank=True)),
                ('pic_url', models.URLField(max_length=255, null=True, verbose_name='\u56fe\u7247url', blank=True)),
                ('shop_type', models.CharField(max_length=2, null=True, verbose_name='\u5e97\u94fa\u7c7b\u578b:B(\u5546\u57ce),C(\u96c6\u5e02)', blank=True)),
                ('open_iid', models.CharField(max_length=255, null=True, verbose_name='\u5546\u54c1ID', blank=True)),
                ('title', models.CharField(max_length=255, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('price', models.DecimalField(null=True, verbose_name='\u4ef7\u683c', max_digits=10, decimal_places=2, blank=True)),
                ('recommend', models.BooleanField(default=False, verbose_name='\u662f\u5426\u63a8\u8350')),
                ('gender', models.CharField(default='female', max_length=20, verbose_name='\u6027\u522b', choices=[('male', '\u7537'), ('female', '\u5973')])),
                ('description', models.TextField(verbose_name='\u8be6\u7ec6\u4fe1\u606f', blank=True)),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u5217\u8868',
                'verbose_name_plural': '\u5546\u54c1\u5217\u8868',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='\u5206\u7c7b\u540d\u79f0')),
                ('slug', models.SlugField(default='', verbose_name='Slug')),
                ('ordering', models.PositiveIntegerField(default=999, verbose_name='\u6392\u5e8f')),
                ('is_active', models.BooleanField(default=False, verbose_name='\u6fc0\u6d3b')),
                ('cover', models.ImageField(upload_to=b'', max_length=200, verbose_name='\u5206\u7c7b\u56fe\u7247', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='restful.GoodsCategory', null=True)),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u7c7b\u522b',
                'verbose_name_plural': '\u5546\u54c1\u7c7b\u522b',
            },
        ),
        migrations.CreateModel(
            name='GoodsItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('pic_url', models.ImageField(upload_to=b'')),
                ('auctionId', models.BigIntegerField(default=0, verbose_name='auctionId')),
                ('categoryId', models.BigIntegerField(default=0, verbose_name='categoryId')),
                ('detail_url', models.URLField(verbose_name='URL')),
                ('checker_runtime', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='dynamic_scraper.SchedulerRuntime', null=True)),
                ('collect_website', models.ForeignKey(blank=True, to='restful.CollectWebsite', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.CharField(default='2016', unique=True, max_length=10, verbose_name='\u5e74\u4efd')),
                ('date', models.TextField(help_text='\u591a\u4e2a\u7528\u9017\u53f7\u5206\u5f00.', null=True, verbose_name='\u4f11\u5e02\u65e5\u671f\u96c6\u5408')),
            ],
            options={
                'ordering': ('-year',),
                'verbose_name': '\u4f11\u5e02\u65e5\u671f',
                'verbose_name_plural': '\u4f11\u5e02\u65e5\u671f',
            },
        ),
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('badge', models.IntegerField(verbose_name='\u5b89\u88c5\u6807\u8bb0')),
                ('timeZone', models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u65f6\u533a')),
                ('deviceToken', models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u4ee4\u724c')),
                ('installationId', models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u7f16\u53f7')),
                ('deviceType', models.CharField(max_length=10, verbose_name='\u8bbe\u5907\u7c7b\u578b', choices=[('ios', 'IOS'), ('android', 'Android')])),
                ('channel', models.CharField(max_length=10, verbose_name='\u63a8\u5e7f\u6e20\u9053', choices=[('1000', '\u5b98\u7f51'), ('1001', '91\u52a9\u624b'), ('1002', '\u767e\u5ea6'), ('1003', '\u5b89\u5353'), ('1004', '\u8c4c\u8c46\u835a'), ('1005', '\u5e94\u7528\u5b9d'), ('1006', '360'), ('1007', '\u5e94\u7528\u6c47'), ('1008', '\u9b45\u65cf'), ('1009', 'N\u591a\u7f51'), ('1010', 'PP\u52a9\u624b'), ('1011', '\u6dd8\u5b9d'), ('1012', '\u673a\u950b\u7f51'), ('1013', '\u91d1\u7acb'), ('1014', '\u5c0f\u7c73'), ('1015', '\u534e\u4e3a'), ('1016', '\u641c\u72d7'), ('1017', '\u5b89\u667a'), ('1018', '\u6c83\u5546\u5e97'), ('1019', 'itools'), ('1020', '\u7535\u4fe1\u7231\u6e38\u620f'), ('1021', '\u4f18\u4ebf\u5e02\u573a'), ('1022', '\u5e94\u7528\u8d1d'), ('1023', 'googleplay'), ('1024', '\u5b89\u7c89\u7f51')])),
            ],
            options={
                'verbose_name': '\u5b89\u88c5\u7edf\u8ba1',
                'verbose_name_plural': '\u5b89\u88c5\u7edf\u8ba1',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('keyword', models.CharField(default='', max_length=200, verbose_name='\u5173\u952e\u8bcd')),
            ],
            options={
                'verbose_name': '\u641c\u7d22\u70ed\u8bcd',
                'verbose_name_plural': '\u641c\u7d22\u70ed\u8bcd',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('imei', models.CharField(default='', max_length=100, verbose_name='\u8bbe\u5907\u53f7\u7801')),
                ('address', models.CharField(max_length=200, verbose_name='\u8be6\u7ec6\u5730\u5740', blank=True)),
                ('coordinate', models.CharField(default='', unique=True, max_length=200, verbose_name='\u4f4d\u7f6e\u5750\u6807')),
                ('owner', models.ForeignKey(verbose_name='\u767b\u5f55\u7528\u6237', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': '\u4f4d\u7f6e\u4fe1\u606f',
                'verbose_name_plural': '\u4f4d\u7f6e\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('is_top', models.BooleanField(default=False, verbose_name='\u6d88\u606f\u7f6e\u9876')),
                ('title', models.CharField(default='', max_length=255, verbose_name='\u6d88\u606f\u6807\u9898')),
                ('content', models.TextField(default='', verbose_name='\u6d88\u606f\u6b63\u6587')),
                ('owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('pk',),
                'verbose_name': '\u7528\u6237\u6d88\u606f',
                'verbose_name_plural': '\u7528\u6237\u6d88\u606f',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('number', models.IntegerField(default=0, verbose_name='\u968f\u673a\u53f7\u7801')),
                ('reward', models.IntegerField(default=0, verbose_name='\u4e2d\u5956\u6982\u7387', blank=True)),
                ('orderid', models.CharField(default='', unique=True, max_length=200, verbose_name='\u6dd8\u5b9d\u8ba2\u5355')),
                ('title', models.CharField(default='', max_length=200, verbose_name='\u5546\u54c1\u6807\u9898')),
                ('open_iid', models.CharField(default='', max_length=200, verbose_name='\u5546\u54c1\u5f00\u653eid')),
                ('exchange', models.DateField(null=True, verbose_name='\u5151\u5956\u65f6\u95f4', blank=True)),
            ],
            options={
                'verbose_name': '\u6dd8\u5b9d\u8ba2\u5355',
                'verbose_name_plural': '\u6dd8\u5b9d\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pics_url', models.ImageField(upload_to=b'', null=True, verbose_name='\u56fe\u7247')),
                ('ordering', models.PositiveIntegerField(verbose_name='\u6392\u5e8f')),
                ('summary', models.CharField(max_length=200, verbose_name='\u56fe\u7247\u63cf\u8ff0', blank=True)),
            ],
            options={
                'verbose_name': '\u5f00\u673a\u56fe\u7247',
                'verbose_name_plural': '\u5f00\u673a\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('switchs', models.BooleanField(default=0, verbose_name='\u8d2d\u4e70\u89c4\u5219')),
                ('content', models.TextField(verbose_name='\u89c4\u5219\u63d0\u793a')),
                ('forward', models.DateField(null=True, verbose_name='\u5f00\u5956\u65f6\u95f4', blank=True)),
                ('first_msg', models.CharField(default='', max_length=200, verbose_name='\u4e00\u4f4d\u4e2d\u5956\u63d0\u793a')),
                ('second_msg', models.CharField(default='', max_length=200, verbose_name='\u4e24\u4f4d\u4e2d\u5956\u63d0\u793a')),
                ('third_msg', models.CharField(default='', max_length=200, verbose_name='\u4e09\u4f4d\u4e2d\u5956\u63d0\u793a')),
                ('first_rate', models.DecimalField(null=True, verbose_name='\u4e00\u4f4d\u4e2d\u5956\u6bd4\u7387', max_digits=10, decimal_places=2)),
                ('second_rate', models.DecimalField(null=True, verbose_name='\u4e24\u4f4d\u4e2d\u5956\u6bd4\u7387', max_digits=10, decimal_places=2)),
                ('third_rate', models.DecimalField(null=True, verbose_name='\u4e09\u4f4d\u4e2d\u5956\u6bd4\u7387', max_digits=10, decimal_places=2)),
            ],
            options={
                'verbose_name': '\u63d0\u793a\u6587\u6848',
                'verbose_name_plural': '\u63d0\u793a\u6587\u6848',
            },
        ),
        migrations.CreateModel(
            name='QueryRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=100, null=True, verbose_name='\u5546\u54c1\u6240\u5728\u5730', blank=True)),
                ('auto_send', models.BooleanField(default=0, verbose_name='\u662f\u5426\u81ea\u52a8\u53d1\u8d27')),
                ('cid', models.IntegerField(help_text='\u8be5ID\u53ef\u4ee5\u901a\u8fc7taobao.itemcats.get\u63a5\u53e3\u83b7\u53d6\u5230\u3002', null=True, verbose_name='\u6807\u51c6\u5546\u54c1\u540e\u53f0\u7c7b\u76eeid', blank=True)),
                ('end_commission_num', models.CharField(help_text='\uff08\u4e0e\u8fd4\u56de\u6570\u636e\u4e2d\u7684commission_num\u5b57\u6bb5\u5bf9\u5e94\uff09\u4e0a\u9650.', max_length=100, null=True, verbose_name='30\u5929\u7d2f\u8ba1\u63a8\u5e7f\u91cf', blank=True)),
                ('end_commission_rate', models.CharField(help_text='\u5982\uff1a2345\u8868\u793a23.45%\u3002\u6ce8\uff1astart_commissionRate\u548cend_commissionRate\u4e00\u8d77\u8bbe\u7f6e\u624d\u6709\u6548\u3002', max_length=100, null=True, verbose_name='\u4f63\u91d1\u6bd4\u7387\u4e0a\u9650', blank=True)),
                ('end_credit', models.CharField(choices=[('1heart', '\u4e00\u5fc3'), ('2heart', '\u4e24\u5fc3'), ('3heart', '\u4e09\u5fc3'), ('4heart', '\u56db\u5fc3'), ('5heart', '\u4e94\u5fc3'), ('1diamond', '\u4e00\u94bb'), ('2diamond', '\u4e24\u94bb'), ('3diamond', '\u4e09\u94bb'), ('4diamond', '\u56db\u94bb'), ('5diamond', '\u4e94\u94bb'), ('1crown', '\u4e00\u51a0'), ('2crown', '\u4e24\u51a0'), ('3crown', '\u4e09\u51a0'), ('4crown', '\u56db\u51a0'), ('5crown', '\u4e94\u51a0'), ('1goldencrown', '\u4e00\u9ec4\u51a0'), ('2goldencrown', '\u4e8c\u9ec4\u51a0'), ('3goldencrown', '\u4e09\u9ec4\u51a0'), ('4goldencrown', '\u56db\u9ec4\u51a0'), ('5goldencrown', '\u4e94\u9ec4\u51a0')], max_length=100, blank=True, help_text='\u53ef\u9009\u503c\u548cstart_credit\u4e00\u6837.start_credit\u7684\u503c\u4e00\u5b9a\u8981\u5c0f\u4e8e\u6216\u7b49\u4e8eend_credit\u7684\u503c\u3002\u6ce8\uff1aend_credit\u4e0estart_credit\u4e00\u8d77\u4f7f\u7528\u624d\u751f\u6548', null=True, verbose_name='\u5356\u5bb6\u4fe1\u7528\u4e0b\u9650')),
                ('end_price', models.CharField(max_length=100, null=True, verbose_name='\u6700\u9ad8\u4ef7\u683c', blank=True)),
                ('end_totalnum', models.CharField(help_text='\uff08\u4e0e\u8fd4\u56de\u5b57\u6bb5volume\u5bf9\u5e94\uff09\u4e0a\u9650\u3002', max_length=100, null=True, verbose_name='\u5546\u54c1\u603b\u6210\u4ea4\u91cf', blank=True)),
                ('guarantee', models.BooleanField(default=0, help_text='\u53ef\u9009\u53c2\u6570, \u9ed8\u8ba4true', verbose_name='\u662f\u5426\u67e5\u8be2\u6d88\u4fdd\u5356\u5bb6')),
                ('real_describe', models.BooleanField(default=0, help_text='\uff08\u4e0e\u8fd4\u56de\u5b57\u6bb5volume\u5bf9\u5e94\uff09\u4e0a\u9650\u3002', verbose_name='\u662f\u5426\u5982\u5b9e\u63cf\u8ff0')),
                ('keyword', models.CharField(help_text=' \u6ce8\u610f:\u67e5\u8be2\u65f6keyword,cid\u81f3\u5c11\u9009\u62e9\u5176\u4e2d\u4e00\u4e2a\u53c2\u6570', max_length=100, null=True, verbose_name='\u5546\u54c1\u6807\u9898\u4e2d\u5305\u542b\u7684\u5173\u952e\u5b57')),
                ('cash_coupon', models.BooleanField(default=0, help_text='\u8bbe\u7f6e\u4e3atrue\u8868\u793a\u8be5\u5546\u54c1\u652f\u6301\u62b5\u4ef7\u5238\uff0c\u8bbe\u7f6e\u4e3afalse\u6216\u4e0d\u8bbe\u7f6e\u8868\u793a\u4e0d\u5224\u65ad\u8fd9\u4e2a\u5c5e\u6027', verbose_name='\u662f\u5426\u652f\u6301\u62b5\u4ef7\u5238')),
                ('vip_card', models.BooleanField(default=0, help_text='\u8bbe\u7f6e\u4e3atrue\u8868\u793a\u8be5\u5546\u54c1\u652f\u6301VIP\u5361\uff0c\u8bbe\u7f6e\u4e3afalse\u6216\u4e0d\u8bbe\u7f6e\u8868\u793a\u4e0d\u5224\u65ad\u8fd9\u4e2a\u5c5e\u6027', verbose_name='\u662f\u5426\u652f\u6301VIP\u5361')),
                ('page_no', models.IntegerField(null=True, verbose_name='\u5206\u9875\u9875\u7801', blank=True)),
                ('page_size', models.IntegerField(null=True, verbose_name='\u5206\u9875\u5927\u5c0f', blank=True)),
                ('overseas_item', models.BooleanField(help_text='\u8bbe\u7f6e\u4e3atrue\u8868\u793a\u8be5\u5546\u54c1\u662f\u5c5e\u4e8e\u6d77\u5916\u5546\u54c1\uff0c\u9ed8\u8ba4\u4e3afalse', verbose_name='\u662f\u5426\u6d77\u5916\u5546\u54c1')),
                ('onemonth_repair', models.BooleanField(default=0, help_text='\u8bbe\u7f6e\u4e3atrue\u8868\u793a\u8be5\u5546\u54c1\u662f\u652f\u630130\u5929\u7ef4\u4fee\uff0c\u8bbe\u7f6e\u4e3afalse\u6216\u4e0d\u8bbe\u7f6e\u8868\u793a\u4e0d\u5224\u65ad\u8fd9\u4e2a\u5c5e\u6027', verbose_name='\u662f\u542630\u5929\u7ef4\u4fee')),
                ('sevendays_return', models.BooleanField(default=0, help_text='\u8bbe\u7f6e\u4e3atrue\u8868\u793a\u8be5\u5546\u54c1\u652f\u63017\u5929\u9000\u6362\uff0c\u8bbe\u7f6e\u4e3afalse\u6216\u4e0d\u8bbe\u7f6e\u8868\u793a\u4e0d\u5224\u65ad\u8fd9\u4e2a\u5c5e\u6027', verbose_name='\u662f\u5426\u652f\u63017\u5929\u9000\u6362')),
                ('sort', models.CharField(max_length=100, null=True, verbose_name='\u9ed8\u8ba4\u6392\u5e8f', choices=[('price_desc', '\u4ef7\u683c\u4ece\u9ad8\u5230\u4f4e'), ('price_asc', '\u4ef7\u683c\u4ece\u4f4e\u5230\u9ad8'), ('credit_desc', '\u4fe1\u7528\u7b49\u7ea7\u4ece\u9ad8\u5230\u4f4e'), ('commissionRate_desc', '\u4f63\u91d1\u6bd4\u7387\u4ece\u9ad8\u5230\u4f4e'), ('commissionRate_asc', '\u4f63\u91d1\u6bd4\u7387\u4ece\u4f4e\u5230\u9ad8'), ('commissionNum_desc', '\u6210\u4ea4\u91cf\u6210\u9ad8\u5230\u4f4e'), ('commissionNum_asc', '\u6210\u4ea4\u91cf\u4ece\u4f4e\u5230\u9ad8'), ('commissionVolume_desc', '\u603b\u652f\u51fa\u4f63\u91d1\u4ece\u9ad8\u5230\u4f4e'), ('commissionVolume_asc', '\u603b\u652f\u51fa\u4f63\u91d1\u4ece\u4f4e\u5230\u9ad8'), ('delistTime_desc', '\u5546\u54c1\u4e0b\u67b6\u65f6\u95f4\u4ece\u9ad8\u5230\u4f4e'), ('delistTime_asc', '\u5546\u54c1\u4e0b\u67b6\u65f6\u95f4\u4ece\u4f4e\u5230\u9ad8')])),
                ('start_commission_num', models.CharField(help_text='\uff08\u4e0e\u8fd4\u56de\u6570\u636e\u4e2d\u7684commission_num\u5b57\u6bb5\u5bf9\u5e94\uff09\u4e0b\u9650.\u6ce8\uff1a\u8be5\u5b57\u6bb5\u8981\u4e0eend_commissionNum\u4e00\u8d77\u4f7f\u7528\u624d\u751f\u6548', max_length=100, null=True, verbose_name='30\u5929\u7d2f\u8ba1\u63a8\u5e7f\u91cf')),
                ('start_commission_rate', models.CharField(help_text='\u5982\uff1a1234\u8868\u793a12.34%', max_length=100, null=True, verbose_name='\u4f63\u91d1\u6bd4\u7387\u4e0b\u9650', blank=True)),
                ('start_credit', models.CharField(max_length=100, null=True, verbose_name='\u5356\u5bb6\u4fe1\u7528\u4e0a\u9650', choices=[('1heart', '\u4e00\u5fc3'), ('2heart', '\u4e24\u5fc3'), ('3heart', '\u4e09\u5fc3'), ('4heart', '\u56db\u5fc3'), ('5heart', '\u4e94\u5fc3'), ('1diamond', '\u4e00\u94bb'), ('2diamond', '\u4e24\u94bb'), ('3diamond', '\u4e09\u94bb'), ('4diamond', '\u56db\u94bb'), ('5diamond', '\u4e94\u94bb'), ('1crown', '\u4e00\u51a0'), ('2crown', '\u4e24\u51a0'), ('3crown', '\u4e09\u51a0'), ('4crown', '\u56db\u51a0'), ('5crown', '\u4e94\u51a0'), ('1goldencrown', '\u4e00\u9ec4\u51a0'), ('2goldencrown', '\u4e8c\u9ec4\u51a0'), ('3goldencrown', '\u4e09\u9ec4\u51a0'), ('4goldencrown', '\u56db\u9ec4\u51a0'), ('5goldencrown', '\u4e94\u9ec4\u51a0')])),
                ('start_price', models.CharField(help_text='\u4f20\u5165\u4ef7\u683c\u53c2\u6570\u65f6,\u9700\u6ce8\u610f\u8d77\u59cb\u4ef7\u683c\u548c\u6700\u9ad8\u4ef7\u683c\u5fc5\u987b\u4e00\u8d77\u4f20\u5165,\u5e76\u4e14 start_price <= end_price', max_length=100, null=True, verbose_name='\u8d77\u59cb\u4ef7\u683c', blank=True)),
                ('start_totalnum', models.CharField(help_text='\uff08\u4e0e\u8fd4\u56de\u5b57\u6bb5volume\u5bf9\u5e94\uff09\u4e0b\u9650\u3002', max_length=100, null=True, verbose_name='\u5546\u54c1\u603b\u6210\u4ea4\u91cf', blank=True)),
                ('support_cod', models.BooleanField(default=0, help_text='\u8bbe\u7f6e\u4e3atrue\u8868\u793a\u8be5\u5546\u54c1\u662f\u652f\u6301\u8d27\u5230\u4ed8\u6b3e\uff0c\u8bbe\u7f6e\u4e3afalse\u6216\u4e0d\u8bbe\u7f6e\u8868\u793a\u4e0d\u5224\u65ad\u8fd9\u4e2a\u5c5e\u6027', verbose_name='\u662f\u5426\u652f\u6301\u8d27\u5230\u4ed8\u6b3e')),
                ('mall_item', models.BooleanField(default=0, help_text='\u8bbe\u7f6e\u4e3atrue\u8868\u793a\u8be5\u5546\u54c1\u662f\u5c5e\u4e8e\u6dd8\u5b9d\u5546\u57ce\u7684\u5546\u54c1\uff0c\u8bbe\u7f6e\u4e3afalse\u6216\u4e0d\u8bbe\u7f6e\u8868\u793a\u4e0d\u5224\u65ad\u8fd9\u4e2a\u5c5e\u6027', verbose_name='\u662f\u5426\u5546\u57ce\u7684\u5546\u54c1')),
            ],
            options={
                'verbose_name': '\u641c\u7d22\u89c4\u5219',
                'verbose_name_plural': '\u641c\u7d22\u89c4\u5219',
            },
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=20, verbose_name='\u5927\u76d8\u6307\u6570')),
                ('today', models.DateField(verbose_name='\u6307\u6570\u65e5\u671f')),
            ],
            options={
                'verbose_name': '\u6307\u6570\u8bb0\u5f55',
                'verbose_name_plural': '\u6307\u6570\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('platform', models.CharField(blank=True, max_length=200, verbose_name='\u624b\u673a\u5e73\u53f0', choices=[('ios', 'IOS'), ('android', 'Android')])),
                ('content', models.TextField(default='', unique=True, verbose_name='\u6dd8\u53e3\u4ee4\u89c4\u5219')),
            ],
            options={
                'verbose_name': '\u53e3\u4ee4\u89c4\u5219',
                'verbose_name_plural': '\u53e3\u4ee4\u89c4\u5219',
            },
        ),
        migrations.CreateModel(
            name='Shared',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('platform', models.CharField(max_length=200, verbose_name='\u5206\u4eab\u5e73\u53f0', choices=[('wechat', '\u5fae\u4fe1'), ('weibo', '\u5fae\u535a'), ('qq', 'QQ')])),
                ('channels', models.CharField(blank=True, max_length=200, verbose_name='\u5206\u4eab\u9891\u9053', choices=[('timeline', '\u670b\u53cb\u5708'), ('friends', '\u5fae\u4fe1\u597d\u53cb')])),
                ('open_iid', models.CharField(default='', max_length=100, verbose_name='\u5546\u54c1\u5f00\u653eID')),
                ('model', models.CharField(default='', max_length=2, verbose_name='\u5206\u4eab\u7c7b\u578b', blank=True, choices=[('1', '\u63a8\u5e7f'), ('2', '\u4e2d\u5956'), ('3', '\u63d0\u73b0')])),
                ('title', models.CharField(max_length=200, verbose_name='\u5546\u54c1\u6807\u9898', blank=True)),
                ('url', models.URLField(null=True, verbose_name='\u5206\u4eabURL', blank=True)),
                ('owner', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u5206\u4eab\u8bb0\u5f55',
                'verbose_name_plural': '\u5206\u4eab\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='SharedRule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('start_date', models.DateField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('end_date', models.DateField(verbose_name='\u8fc7\u671f\u65f6\u95f4')),
                ('number', models.IntegerField(default='1', verbose_name='\u5206\u4eab\u6b21\u6570')),
                ('price', models.FloatField(default='0.00', verbose_name='\u5956\u52b1\u91d1\u989d')),
            ],
            options={
                'verbose_name': '\u5206\u4eab\u89c4\u5219',
                'verbose_name_plural': '\u5206\u4eab\u89c4\u5219',
            },
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('summary', models.CharField(default='', max_length=100, verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'ordering': ('pk',),
                'verbose_name': '\u6a2a\u5e45\u5e7f\u544a',
                'verbose_name_plural': '\u6a2a\u5e45\u5e7f\u544a',
            },
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first', models.IntegerField(default='0', verbose_name='\u4e00\u4f4d\u6570')),
                ('second', models.IntegerField(default='0', verbose_name='\u4e24\u4f4d\u6570')),
                ('third', models.IntegerField(default='0', verbose_name='\u4e09\u4f4d\u6570')),
                ('number', models.IntegerField(default='0', verbose_name='\u5151\u5956\u6570\u5b57')),
                ('exchange', models.DateField(null=True, verbose_name='\u5151\u5956\u65f6\u95f4', blank=True)),
            ],
            options={
                'verbose_name': '\u4e2d\u5956\u6a21\u62df\u6570\u636e',
                'verbose_name_plural': '\u4e2d\u5956\u6a21\u62df',
            },
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('number', models.IntegerField(default=0, verbose_name='\u968f\u673a\u53f7\u7801')),
                ('reward', models.IntegerField(default=0, verbose_name='\u4e2d\u5956\u6982\u7387', blank=True)),
                ('orderid', models.CharField(default='', unique=True, max_length=200, verbose_name='\u6dd8\u5b9d\u8ba2\u5355')),
                ('title', models.CharField(default='', max_length=200, verbose_name='\u5546\u54c1\u6807\u9898')),
                ('pic_url', models.URLField(default='', verbose_name='\u56fe\u7247\u7f51\u5740')),
                ('open_iid', models.CharField(default='', max_length=200, verbose_name='\u5546\u54c1\u5f00\u653eid')),
                ('price', models.DecimalField(default=0.0, verbose_name='\u4ef7\u683c', max_digits=10, decimal_places=2)),
                ('num', models.IntegerField(default=1, verbose_name='\u6570\u91cf', blank=True)),
                ('exchange', models.DateField(null=True, verbose_name='\u5151\u5956\u65f6\u95f4', blank=True)),
                ('owner', models.ForeignKey(verbose_name='\u767b\u5f55\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u4ea4\u6613\u8bb0\u5f55',
                'verbose_name_plural': '\u4ea4\u6613\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('version', models.CharField(default='1.0.0', max_length=10, verbose_name='\u7248\u672c\u53f7')),
                ('install', models.FileField(upload_to='install', null=True, verbose_name='\u5b89\u88c5\u8fde\u63a5')),
                ('sha1sum', models.CharField(max_length=64, verbose_name='\u6587\u4ef6\u9a8c\u8bc1\u7801')),
                ('channel', models.CharField(max_length=10, verbose_name='\u63a8\u5e7f\u6e20\u9053', choices=[('1000', '\u5b98\u7f51'), ('1001', '91\u52a9\u624b'), ('1002', '\u767e\u5ea6'), ('1003', '\u5b89\u5353'), ('1004', '\u8c4c\u8c46\u835a'), ('1005', '\u5e94\u7528\u5b9d'), ('1006', '360'), ('1007', '\u5e94\u7528\u6c47'), ('1008', '\u9b45\u65cf'), ('1009', 'N\u591a\u7f51'), ('1010', 'PP\u52a9\u624b'), ('1011', '\u6dd8\u5b9d'), ('1012', '\u673a\u950b\u7f51'), ('1013', '\u91d1\u7acb'), ('1014', '\u5c0f\u7c73'), ('1015', '\u534e\u4e3a'), ('1016', '\u641c\u72d7'), ('1017', '\u5b89\u667a'), ('1018', '\u6c83\u5546\u5e97'), ('1019', 'itools'), ('1020', '\u7535\u4fe1\u7231\u6e38\u620f'), ('1021', '\u4f18\u4ebf\u5e02\u573a'), ('1022', '\u5e94\u7528\u8d1d'), ('1023', 'googleplay'), ('1024', '\u5b89\u7c89\u7f51')])),
                ('platform', models.CharField(default='android', max_length=50, verbose_name='APP\u5e73\u53f0', choices=[('ios', 'IOS'), ('android', 'Android')])),
            ],
            options={
                'verbose_name': '\u7248\u672c\u5347\u7ea7',
                'verbose_name_plural': '\u7248\u672c\u5347\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='Watchword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('watchword', models.TextField(default='', max_length=200, verbose_name='\u53e3\u4ee4')),
                ('sort', models.CharField(default='price_asc', max_length=20, verbose_name='\u6392\u5e8f\u65b9\u5f0f', choices=[('price_asc', '\u4ef7\u683c\u5347\u5e8f'), ('price_desc', '\u4ef7\u683c\u5012\u5e8f')])),
            ],
            options={
                'verbose_name': '\u6dd8\u5ba2\u53e3\u4ee4',
                'verbose_name_plural': '\u6dd8\u5ba2\u53e3\u4ee4',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(verbose_name='\u5546\u54c1\u5206\u7c7b', to='restful.GoodsCategory', null=True),
        ),
        migrations.AddField(
            model_name='firstprize',
            name='prizegoods',
            field=models.ForeignKey(to='restful.Goods'),
        ),
    ]
