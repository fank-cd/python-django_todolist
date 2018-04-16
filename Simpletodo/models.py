# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=10)
    description = models.CharField(max_length=100, null=True, blank=True)
    pubtime = models.DateTimeField(auto_now_add=True)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name
