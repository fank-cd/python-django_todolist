# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from defaulttodo.froms import UserForm, BiuForm, ItemForm
from defaulttodo.models import Item
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    item_list = []
    item_list_done = []
    if request.user.is_authenticated():
        user = request.user
        item_list = Item.objects.filter(
            user=user, flag=False).order_by('-priority')
        item_list_done = Item.objects.filter(
            user=user, flag=True).order_by('-pub_time')[:5]
        #print type(item_list)

    context = {'item_list': item_list, 'item_list_done': item_list_done}
    return render(request, 'default/index.html', context=context)


@login_required()
def notfinish_item(request, pk):
    i = get_object_or_404(Item, pk=pk)
    if i.flag:
        i.flag = False
        i.save()
    return HttpResponseRedirect('/default/')


@login_required()
def tofinish_item(request, pk):
    i = get_object_or_404(Item, pk=pk)
    print i.flag
    if not i.flag:
        i.flag = True
        i.save()
        return HttpResponseRedirect('/default/')


@login_required()
def update_item(request, pk):
    i = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item_form = ItemForm(data=request.POST, instance=i)
        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.item_name = request.POST.get('item_name')
            item.item_description = request.POST.get('item_description')
            item.proiorty = request.POST.get('proiorty')
            item.user = request.user
            item.save()
            return HttpResponseRedirect('/default/')
        else:
            print item_form.errors
    else:
        item_form = ItemForm()
    context = {'item_form': item_form, 'i': i}
    return render(request, 'default/update_item.html', context=context)


@login_required()
def item_detail(request, pk):
    i = get_object_or_404(Item, pk=pk)
    item_name = i.item_name
    item_description = i.item_description
    pub_time = i.pub_time
    item_id = i.id
    item_flag = i.flag
    context = {
        'item_name': item_name,
        'item_description': item_description,
        'pub_time': pub_time,
        'item_id': item_id,
        'item_flag': item_flag
    }
    return render(request, 'default/item_detail.html', context=context)


@login_required()
def delete_item(request, pk):
    i = get_object_or_404(Item, pk=pk)
    i.flag = True
    i.delete()
    return HttpResponseRedirect('/default/')


@login_required()
def add_item(request):
    if request.method == "POST":
        item_form = ItemForm(data=request.POST)
        #print request.user.id

        if item_form.is_valid():
            item = item_form.save(commit=False)
            item.item_name = request.POST.get('item_name')
            item.item_description = request.POST.get('item_description')
            item.proiorty = request.POST.get('proiorty')
            item.user = request.user
            item.save()
            return HttpResponseRedirect('/default/')
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


