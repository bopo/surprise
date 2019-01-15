# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import restful.contrib.consumer.models
import imagekit.models.fields
import model_utils.fields
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('mobile', models.CharField(db_index=True, max_length=25, verbose_name='\u624b\u673a\u53f7\u7801', blank=True)),
                ('verify_code', models.CharField(max_length=5, verbose_name='\u77ed\u4fe1\u7801', blank=True)),
                ('device', models.CharField(max_length=100, verbose_name='\u8bbe\u5907\u53f7')),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', restful.contrib.consumer.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default='open', max_length=100, verbose_name='status', no_check_for_status=True, choices=[('open', 'open'), ('close', 'close')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('full_name', models.CharField(max_length=200, verbose_name='\u6536\u4fe1\u4eba')),
                ('city', models.CharField(max_length=200, verbose_name='\u57ce\u5e02')),
                ('address', models.CharField(max_length=200, verbose_name='\u8be6\u7ec6\u5730\u5740')),
                ('mobile', models.CharField(default='0', max_length=20, verbose_name='\u79fb\u52a8\u7535\u8bdd')),
                ('owner', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Behavior',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(default=None, blank=True, to='contenttypes.ContentType')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': '\u7528\u6237\u884c\u4e3a',
                'verbose_name_plural': '\u7528\u6237\u884c\u4e3a',
            },
        ),
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('ip', models.GenericIPAddressField(default='0.0.0.0', verbose_name='\u767b\u5f55ip')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u767b\u5f55\u8bb0\u5f55',
                'verbose_name_plural': '\u767b\u5f55\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Extract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default='ready', max_length=100, verbose_name='status', no_check_for_status=True, choices=[('ready', '\u5f85\u5904\u7406'), ('rejected', '\u5df2\u9a73\u56de'), ('success', '\u5df2\u5b8c\u6210')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('price', models.DecimalField(null=True, verbose_name='\u63d0\u73b0\u91d1\u989d', max_digits=10, decimal_places=2)),
                ('alipay', models.CharField(default='', max_length=100, verbose_name='\u652f\u4ed8\u5b9d')),
                ('full_name', models.CharField(default='', max_length=100, verbose_name='\u7528\u6237\u59d3\u540d')),
                ('is_share', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5206\u4eab')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u63d0\u73b0\u8bb0\u5f55',
                'verbose_name_plural': '\u63d0\u73b0\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(default=None, blank=True, to='contenttypes.ContentType')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6536\u85cf\u5939',
                'verbose_name_plural': '\u6536\u85cf\u5939',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default='ready', max_length=100, verbose_name='status', no_check_for_status=True, choices=[('ready', 'ready'), ('unread', 'unread')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('choices', models.CharField(max_length=100, null=True, verbose_name='\u53cd\u9988\u7c7b\u578b')),
                ('content', models.TextField(null=True, verbose_name='\u53cd\u9988\u5185\u5bb9')),
                ('contact', models.CharField(default='', max_length=200, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('owner', models.ForeignKey(related_name='follows', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='fans', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u5173\u6ce8',
                'verbose_name_plural': '\u5173\u6ce8',
            },
        ),
        migrations.CreateModel(
            name='Geographic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('latitude', models.FloatField(verbose_name='latitude')),
                ('longitude', models.FloatField(verbose_name='longitude')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User geographic',
                'verbose_name_plural': 'User geographic',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(default=None, blank=True, to='contenttypes.ContentType')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6211\u559c\u6b22',
                'verbose_name_plural': '\u6211\u559c\u6b22',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('title', models.CharField(default='', max_length=255, verbose_name='\u6536\u85cf\u5185\u5bb9\u7684\u6807\u9898')),
                ('url', models.CharField(default='', max_length=255, verbose_name='\u6536\u85cf\u5185\u5bb9\u7684\u539f\u6587\u5730\u5740\uff0c\u4e0d\u5e26\u57df\u540d')),
                ('summary', models.CharField(default='', max_length=255, verbose_name='\u6536\u85cf\u5185\u5bb9\u7684\u63cf\u8ff0')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('score', models.IntegerField(default=0)),
                ('event', models.ForeignKey(default=0, to='contenttypes.ContentType')),
                ('owner', models.ForeignKey(verbose_name='credits', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u79ef\u5206\u8bb0\u5f55',
                'verbose_name_plural': '\u79ef\u5206\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('owner', models.OneToOneField(related_name='settings', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7b7e\u5230\u8bb0\u5f55',
                'verbose_name_plural': '\u7b7e\u5230\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='SmsCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default='open', max_length=100, verbose_name='status', no_check_for_status=True, choices=[('open', 'open'), ('close', 'close')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('code', models.CharField(unique=True, max_length=128, verbose_name='\u77ed\u4fe1\u9a8c\u8bc1\u7801')),
                ('user', models.OneToOneField(related_name='smscode', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('from_user', models.ForeignKey(related_name='from_user', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='\u59d3\u540d', blank=True)),
                ('nick', models.CharField(db_index=True, max_length=255, null=True, verbose_name='\u6635\u79f0', blank=True)),
                ('phone', models.CharField(default='', max_length=64, verbose_name='\u7535\u8bdd', blank=True)),
                ('gender', models.CharField(default='male', max_length=10, verbose_name='\u6027\u522b', choices=[('male', '\u7537'), ('female', '\u5973')])),
                ('zodiac', models.CharField(max_length=25, verbose_name='\u661f\u5ea7', blank=True)),
                ('birthday', models.DateField(null=True, verbose_name='\u751f\u65e5', blank=True)),
                ('alipay', models.CharField(max_length=100, verbose_name='\u652f\u4ed8\u5b9d', blank=True)),
                ('qq', models.CharField(max_length=100, verbose_name='QQ', blank=True)),
                ('chinese_zodiac', models.CharField(max_length=25, verbose_name='\u751f\u8096', blank=True)),
                ('payment', models.DecimalField(default=0.0, verbose_name='\u5df2\u7ecf\u63d0\u73b0', max_digits=10, decimal_places=2)),
                ('balance', models.DecimalField(default=0.0, verbose_name='\u5e10\u6237\u4f59\u989d', max_digits=10, decimal_places=2)),
                ('total', models.DecimalField(default=0.0, verbose_name='\u5e10\u6237\u603b\u989d', max_digits=10, decimal_places=2)),
                ('avatar', imagekit.models.fields.ProcessedImageField(upload_to='avatar', null=True, verbose_name='\u5934\u50cf')),
                ('owner', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]
