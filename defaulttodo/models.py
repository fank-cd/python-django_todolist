# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
#from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


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

class Biu(models.Model):
    biu = models.CharField(max_length=120)

    def __unicode__(self):
        return self.biu