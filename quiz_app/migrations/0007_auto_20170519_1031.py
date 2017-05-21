# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-19 07:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz_app', '0006_auto_20170518_2038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='count_all',
        ),
        migrations.RemoveField(
            model_name='task',
            name='count_true',
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
        migrations.AddField(
            model_name='tagtask',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]