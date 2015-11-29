# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_management', '0015_auto_20151129_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='attitude',
            field=models.DecimalField(verbose_name=b'Attitude', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='class_participation',
            field=models.DecimalField(verbose_name=b'Class Participation', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='commitment',
            field=models.DecimalField(verbose_name=b'Commitment', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='english_fluency',
            field=models.DecimalField(verbose_name=b'English Fluency', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='month',
            field=models.CharField(default=b'January', max_length=20, choices=[(b'January', b'January'), (b'February', b'February'), (b'March', b'March'), (b'April', b'April'), (b'May', b'May'), (b'June', b'June'), (b'July', b'July'), (b'August', b'August'), (b'September', b'September'), (b'October', b'October'), (b'November', b'November'), (b'December', b'December')]),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='practical_mark',
            field=models.DecimalField(verbose_name=b'Practical Mark', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='presentation_skills',
            field=models.DecimalField(verbose_name=b'Presentaion Skills', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='punctuality',
            field=models.DecimalField(verbose_name=b'Punctuality', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='theory_mark',
            field=models.DecimalField(verbose_name=b'Theory Mark', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
