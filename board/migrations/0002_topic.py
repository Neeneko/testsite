# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('title', models.CharField(max_length=256)),
                ('desc', models.TextField()),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Author')),
            ],
        ),
    ]
