# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-16 14:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20170516_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='onyoumi',
            new_name='onyomi',
        ),
    ]
