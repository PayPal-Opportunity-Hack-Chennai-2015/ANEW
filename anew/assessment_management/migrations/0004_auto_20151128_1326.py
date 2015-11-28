# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assessment_management', '0003_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name=b'Name')),
                ('start_date', models.DateField(auto_now=True, verbose_name=b'Start Date')),
                ('end_date', models.DateField(auto_now=True, verbose_name=b'End Date')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name=b'created Date')),
                ('updatedon', models.DateTimeField(auto_now=True, verbose_name=b'Updated Date')),
            ],
        ),
        migrations.CreateModel(
            name='Timings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.TimeField(auto_now=True, verbose_name=b'Start Time')),
                ('end_time', models.TimeField(auto_now=True, verbose_name=b'End Time')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name=b'created Date')),
                ('updatedon', models.DateTimeField(auto_now=True, verbose_name=b'Updated Date')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together=set([('name', 'location')]),
        ),
        migrations.AddField(
            model_name='batch',
            name='timing',
            field=models.ForeignKey(to='assessment_management.Timings'),
        ),
        migrations.AddField(
            model_name='batch',
            name='tutor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
