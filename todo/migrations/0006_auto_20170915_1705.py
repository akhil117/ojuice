# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-15 15:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0005_auto_20170728_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='owner',
        ),
        migrations.AddField(
            model_name='todo',
            name='owner',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
