# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-13 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20170513_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание'),
        ),
    ]