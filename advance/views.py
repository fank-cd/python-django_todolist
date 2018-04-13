# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from advance.models import User,Item_advance
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    item_list = []
    if request.user.is_authenticated():
        user = request.user
        item_list = Item_advance.objects.filter(
            user=user, flag=False).order_by('-item_prority')
    context = {'item_list': item_list}
    return render(request, 'advance/index.html', context=context)

@login_required(login_url='/advance/login')

def list(requset):
    item_list = []
    item_donelist = []
    if requset.user.is_authenticated():
        user = requset.user
        item_list = Item_advance.objects.filter(
            user=user,flag =False).order_by('pub_time')

        item_donelist = Item_advance.objects.filter(
            user=user, flag=True).order_by('-pub_time')

    context ={'item_list':item_list,'item_donelist':item_donelist}

    return render(requset,'advance/list.html',context=context)

@login_required(login_url='/advance/login')
def item_detail(request,pk):
    i = get_object_or_404(Item_advance, pk=pk)
    item_name = i.item_name
    item_description = i.item_descrip
    item_prority = i.item_prority
    item_id = i.id
    item_flag = i.flag
    pub_time = i.pub_time
    context = {
        'item_name': item_name,
        'item_description': item_description,
        'pub_time': pub_time,
        'item_id': item_id,
        'item_flag': item_flag,
        'item_prority':item_prority,
    }
    return render(request, 'advance/item_detail.html', context=context)



@login_required(login_url='/advance/login')
def add_item(request):

    if request.method == "POST":
        item = Item_advance()
        item.item_name = request.POST.get('itemname')
        item.item_descrip = request.POST.get('itemdescription')
        item.item_prority = request.POST.get('itempriority')
        item.user = request.user
        item.save()
        return HttpResponseRedirect('/advance')

    return render(request,'advance/add_item.html')


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
        #print username,password
        user = authenticate(username=username, password=password)
        if user:
            print "POSTdsfdasfdasfdasfasdfdasf"
            if user.is_active:
                login(request, user)
                #print "dddddd"
                return HttpResponseRedirect('/advance/')
            else:
                return HttpResponse('your account is invaild')
        else:
            return HttpResponse("invalid login")

    else:
        return render(request, 'advance/login.html', {})

def user_logout(request):
    logout(request=request)
    return HttpResponseRedirect('/advance/')