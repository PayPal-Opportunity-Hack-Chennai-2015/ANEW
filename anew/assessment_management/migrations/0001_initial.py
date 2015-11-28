# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reg_no', models.CharField(unique=True, max_length=40, verbose_name=b'Registration Number')),
                ('college_name', models.CharField(max_length=40, null=True, verbose_name=b'College Name', blank=True)),
                ('age', models.IntegerField(null=True, verbose_name=b'Age', blank=True)),
                ('phone_number', models.IntegerField(null=True, verbose_name=b'Phone Number', blank=True)),
                ('address', models.CharField(max_length=100, null=True, verbose_name=b'Address', blank=True)),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name=b'created Date')),
                ('updatedon', models.DateTimeField(auto_now=True, verbose_name=b'Updated Date')),
                ('user', models.OneToOneField(verbose_name=b'User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
