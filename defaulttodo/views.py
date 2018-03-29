# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from defaulttodo.froms import UserForm, BiuForm, ItemForm
from django.shortcuts import redirect
from defaulttodo.models import Item
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    item_list = []
    if request.user.is_authenticated():
        print "dd"
        user= request.user
        item_list = Item.objects.filter(user=user).order_by('-priority')
        print item_list
    context = {'item_list':item_list}
    return render(request, 'default/index.html', context=context)

@login_required()
def add_item(request):
    if request.method == "POST":
        item_form = ItemForm(data=request.POST)
        print request.user.id

        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.item_name = request.POST.get('item_name')
            item.item_description = request.POST.get('item_description')
            item.proiorty = request.POST.get('proiorty')
            item.user =request.user
            item.save()
        else:
            print item_form.errors
    else:
        item_form = ItemForm()
    context = {'item_form': item_form}
    return render(request, 'default/add_item.html', context=context)



def resgister(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()

    context = {'user_form': user_form, 'registered': registered}
    return render(request, 'default/register.html', context=context)


def user_login(request):
    if request.method == 'POST':
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
        # because the request.POST.get('<variable>') returns None, if the value does not exist,
        # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            print "POSTdsfdasfdasfdasfasdfdasf"
            if user.is_active:
                login(request, user)
                print "dddddd"
                return HttpResponseRedirect('/default/')
            else:
                return HttpResponse('your account is invaild')
        else:
            return HttpResponse("invalid login")

    else:
        return render(request, 'default/login.html', {})


@login_required()
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/default')


def zanshi(request):
    if request.method == "POST":
        form = BiuForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.biu = request.POST['biu']
            #instance.biu =request.POST.get('bi1u')
            instance.save()
    else:
        form = BiuForm()
    return render(request, 'default/zanshi.html', {'form': form})
