# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_management', '0012_auto_20151129_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbatch',
            name='student',
            field=smart_selects.db_fields.GroupedForeignKey(to='assessment_management.Student', group_field=b'batch'),
        ),
    ]
