# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-26 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('defaulttodo', '0002_auto_20180326_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biu', models.CharField(max_length=120)),
            ],
        ),
    ]
