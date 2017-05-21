# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-19 16:26
from __future__ import unicode_literals

from django.db import migrations, models
import quiz_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0010_auto_20170519_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=quiz_app.models.upload_location, verbose_name='Изображение'),
        ),
    ]
