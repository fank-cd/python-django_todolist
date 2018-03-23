# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-16 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('pubtime', models.DateTimeField(auto_now_add=True)),
                ('flag', models.BooleanField(default=False)),
            ],
        ),
    ]
