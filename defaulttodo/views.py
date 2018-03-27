# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .froms import UserForm,BiuForm
from django.shortcuts import redirect
from .models import Item,User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    logged =False
    if request.user.is_authenticated():
        logged = True

    context = {'logged':logged}
    return render(request,'default/index.html',context=context)


def resgister(request):
    registered =False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered =True
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    context ={'user_form':user_form,'registered':registered}
    return render(request,'default/register.html',context=context)

def user_login(request):
    if request.method == 'POST':
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
        # because the request.POST.get('<variable>') returns None, if the value does not exist,
        # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            print "POSTdsfdasfdasfdasfasdfdasf"
            if user.is_active:
                login(request,user)
                print "dddddd"
                return HttpResponseRedirect('/default/')
            else:
                return HttpResponse('your account is invaild')
        else:
            return HttpResponse("invalid login")

    else:
        return render(request,'default/login.html',{})
@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/default')

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