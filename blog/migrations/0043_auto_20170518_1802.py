# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-18 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_auto_20170518_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='task',
        ),
        migrations.RemoveField(
            model_name='tasktheme',
            name='task',
        ),
        migrations.RemoveField(
            model_name='tasktheme',
            name='theme',
        ),
        migrations.RemoveField(
            model_name='taskword',
            name='task',
        ),
        migrations.RemoveField(
            model_name='taskword',
            name='word',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='TaskTheme',
        ),
        migrations.DeleteModel(
            name='TaskWord',
        ),
    ]
