# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assessment_management', '0006_auto_20151128_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentBatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name=b'created Date')),
                ('updatedon', models.DateTimeField(auto_now=True, verbose_name=b'Updated Date')),
                ('batch', models.ForeignKey(to='assessment_management.Batch')),
                ('student', models.ForeignKey(to='assessment_management.Student')),
            ],
            options={
                'verbose_name': 'Student Batch',
                'verbose_name_plural': 'Student Batches',
            },
        ),
        migrations.CreateModel(
            name='TutorBatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name=b'created Date')),
                ('updatedon', models.DateTimeField(auto_now=True, verbose_name=b'Updated Date')),
                ('batch', models.ForeignKey(to='assessment_management.Batch')),
                ('tutor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tutor Batch',
                'verbose_name_plural': 'Tutor Batches',
            },
        ),
    ]
