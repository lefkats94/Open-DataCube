# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2021-01-26 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('username', models.CharField(max_length=30)),
                ('url', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reset',
            fields=[
                ('username', models.CharField(max_length=30)),
                ('url', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
