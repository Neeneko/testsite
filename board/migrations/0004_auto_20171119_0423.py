# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 04:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20171119_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]