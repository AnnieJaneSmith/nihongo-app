# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-11 12:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161222_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_title', models.CharField(max_length=350, verbose_name='Название темы')),
            ],
            options={
                'verbose_name': 'тема',
                'verbose_name_plural': 'темы',
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_title', models.CharField(max_length=200, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'раздел',
                'verbose_name_plural': 'разделы',
            },
        ),
        migrations.AddField(
            model_name='theme',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Unit'),
        ),
    ]
