# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_management', '0010_auto_20151128_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='month',
            field=models.CharField(default=1, max_length=20, choices=[(1, b'January'), (2, b'February'), (3, b'March'), (4, b'April'), (5, b'May'), (6, b'June'), (7, b'July'), (8, b'August'), (9, b'September'), (10, b'October'), (11, b'November'), (12, b'December')]),
        ),
    ]
