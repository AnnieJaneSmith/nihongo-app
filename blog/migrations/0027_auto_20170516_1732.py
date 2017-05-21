# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-16 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20170516_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translate',
            name='word',
        ),
        migrations.AddField(
            model_name='word',
            name='translation',
            field=models.TextField(blank=True, max_length=530, null=True, verbose_name='Перевод'),
        ),
        migrations.DeleteModel(
            name='Translate',
        ),
    ]