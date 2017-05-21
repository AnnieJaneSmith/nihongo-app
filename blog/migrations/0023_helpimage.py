# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-14 12:36
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_help_inner_unit'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350, verbose_name='Название')),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location, verbose_name='Изображение')),
                ('help', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Help')),
            ],
        ),
    ]