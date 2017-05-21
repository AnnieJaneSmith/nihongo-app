# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-18 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0004_auto_20170518_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='countall',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='counttrue',
        ),
        migrations.AddField(
            model_name='tagtask',
            name='count_all',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tagtask',
            name='count_true',
            field=models.IntegerField(default=0),
        ),
    ]