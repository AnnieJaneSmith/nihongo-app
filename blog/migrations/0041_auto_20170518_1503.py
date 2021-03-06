# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-18 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_auto_20170517_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskTheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Task')),
                ('theme', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Theme')),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='type',
        ),
        migrations.AddField(
            model_name='answer',
            name='ok',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
