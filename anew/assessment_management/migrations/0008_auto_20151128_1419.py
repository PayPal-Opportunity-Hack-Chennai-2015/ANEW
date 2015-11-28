# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('assessment_management', '0007_studentbatch_tutorbatch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('theory_mark', models.DecimalField(verbose_name=b'Theory Mark', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(100)])),
                ('practical_mark', models.DecimalField(verbose_name=b'Practical Mark', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(100)])),
                ('presentation_skills', models.DecimalField(verbose_name=b'Presentaion Skills', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(100)])),
                ('punctuality', models.DecimalField(verbose_name=b'Punctuality', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(100)])),
                ('attitude', models.DecimalField(verbose_name=b'Attitude', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(100)])),
                ('class_participation', models.DecimalField(verbose_name=b'Class Participation', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(100)])),
                ('commitment', models.DecimalField(verbose_name=b'Commitment', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(100)])),
                ('english_fluency', models.DecimalField(verbose_name=b'English Fluency', max_digits=12, decimal_places=2, validators=[django.core.validators.MaxValueValidator(0), django.core.validators.MinValueValidator(100)])),
                ('remarks', models.CharField(max_length=40, verbose_name=b'Remarks')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name=b'created Date')),
                ('updatedon', models.DateTimeField(auto_now=True, verbose_name=b'Updated Date')),
                ('student_batch', models.ForeignKey(to='assessment_management.StudentBatch')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40, verbose_name=b'Title')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name=b'created Date')),
                ('updatedon', models.DateTimeField(auto_now=True, verbose_name=b'Updated Date')),
            ],
        ),
        migrations.AddField(
            model_name='assessment',
            name='subject',
            field=models.ForeignKey(to='assessment_management.Subject'),
        ),
    ]
