# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-26 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defaulttodo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=120),
        ),
    ]