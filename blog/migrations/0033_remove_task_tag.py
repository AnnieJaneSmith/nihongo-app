# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-16 19:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_remove_task_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tag',
        ),
    ]