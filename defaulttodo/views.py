# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .froms import UserForm
from .models import Item,User
# Create your views here.

def index(request):
    return render(request,'default/index.html')


def login(request):
    return HttpResponse('dddddd')

def resgister(request):
    if request.method == "POST":
        user_form =UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.pass