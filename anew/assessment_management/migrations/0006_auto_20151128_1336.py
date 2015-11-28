# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_management', '0005_auto_20151128_1329'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name': 'Batch', 'verbose_name_plural': 'Batches'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='timings',
            options={'verbose_name': 'Timing', 'verbose_name_plural': 'Timings'},
        ),
    ]
