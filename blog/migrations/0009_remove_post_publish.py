# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-11 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170511_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publish',
        ),
    ]
