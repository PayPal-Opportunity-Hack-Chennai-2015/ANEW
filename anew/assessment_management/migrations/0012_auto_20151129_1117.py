# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_management', '0011_auto_20151128_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbatch',
            name='student',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'Batch', chained_field=b'batch', auto_choose=True, to='assessment_management.Student'),
        ),
    ]
