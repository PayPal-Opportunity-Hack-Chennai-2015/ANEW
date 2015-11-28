# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_management', '0004_auto_20151128_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='end_date',
            field=models.DateField(verbose_name=b'End Date'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='start_date',
            field=models.DateField(verbose_name=b'Start Date'),
        ),
        migrations.AlterField(
            model_name='timings',
            name='end_time',
            field=models.TimeField(verbose_name=b'End Time'),
        ),
        migrations.AlterField(
            model_name='timings',
            name='start_time',
            field=models.TimeField(verbose_name=b'Start Time'),
        ),
    ]
