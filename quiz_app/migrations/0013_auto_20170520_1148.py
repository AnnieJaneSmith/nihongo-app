# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-20 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0012_usertask_prev_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='prev_date',
            field=models.DateTimeField(verbose_name='Последний раз пройдено'),
        ),
    ]
