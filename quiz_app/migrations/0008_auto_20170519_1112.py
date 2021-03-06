# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-19 08:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz_app', '0007_auto_20170519_1031'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_all', models.IntegerField(default=0)),
                ('count_true', models.IntegerField(default=0)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz_app.Task')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='tagtask',
            name='count_all',
        ),
        migrations.RemoveField(
            model_name='tagtask',
            name='count_true',
        ),
        migrations.RemoveField(
            model_name='tagtask',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='tagtask',
            name='user',
        ),
    ]
