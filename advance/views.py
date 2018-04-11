# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from advance.models import User,Item_advance
from advance.forms import UserForm,ItemForm
from django.contrib.auth import authenticate,logout,login
# Create your views here.

def index(request):
    return render(request,'advance/index.html')

def register(request):


    if request.method == "POST":
        user = User()

        user.username = request.POST['username']
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponseRedirect('/advance/')


    return render(request, 'advance/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print username,password
        user = authenticate(username=username, password=password)
        if user:
            print "POSTdsfdasfdasfdasfasdfdasf"
            if user.is_active:
                login(request, user)
                print "dddddd"
                return HttpResponseRedirect('/advance/')
            else:
                return HttpResponse('your account is invaild')
        else:
            return HttpResponse("invalid login")

    else:
        return render(request, 'advance/login.html', {})
