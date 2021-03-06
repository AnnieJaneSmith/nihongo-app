# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-12 14:49
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170512_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Заголовок')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=blog.models.upload_location, verbose_name='Изображение')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-timestamp', 'updated'],
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
        migrations.AddField(
            model_name='unit',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AddField(
            model_name='theme',
            name='inner_unit',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='blog.Unit'),
            preserve_default=False,
        ),
    ]
