# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-28 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defaulttodo', '0005_auto_20180328_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=20),
        ),
    ]
