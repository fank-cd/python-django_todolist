# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class item_advance (models.Model):
    item_name = models.CharField(max_length=60)
    item_descrip = models.CharField(max_length=120)
    item_prority = models.IntegerField()
    flag = models.BooleanField(default=False)
    pub_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.item_name

    class Meta:
        ordering = ['-item_prority', 'pub_time']
