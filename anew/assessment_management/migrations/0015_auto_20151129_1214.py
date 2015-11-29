# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_management', '0014_auto_20151129_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbatch',
            name='student',
            field=models.ForeignKey(to='assessment_management.Student'),
        ),
    ]
