# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=120)
    user_pass = models.CharField(max_length=120)

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    item_description = models.CharField(max_length=120,blank=True,null=True)
    flag = models.BooleanField(default=False)
    pub_time =models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField()
    user =models.ForeignKey(User,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.item_name

    class Meta:
        ordering = ['-priority','pub_time']

