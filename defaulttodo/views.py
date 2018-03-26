# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .froms import UserForm,BiuForm
from django.shortcuts import redirect
from .models import Item,User
# Create your views here.

def index(request):
    return render(request,'default/index.html')


def login(request):

    return HttpResponse('dddddd')


def resgister(request):
    #regis = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.name = request.POST['user_name']
            user.passowrd = request.POST['user_pass']
            user.save()
        else:
            print form.errors
    else:
        form = UserForm()

    return render(request,'default/register.html',{'form':form})


def zanshi(request):
    if request.method =="POST":
        form =BiuForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.biu=request.POST['biu']
            #instance.biu =request.POST.get('bi1u')
            instance.save()
    else:
        form = BiuForm()
    return render(request,'default/zanshi.html',{'form':form})