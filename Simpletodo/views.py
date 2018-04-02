# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from models import Item
from django.http import HttpResponseRedirect
# Create your views here.


def index(request):
    item_list = Item.objects.order_by('id')
    #print item_list
    return render(
        request,
        'Simpletodo/index.html',
        context={
            'item': item_list})


def add_new(request):
    if request.method == "POST":
        i = Item()
        i.item_name = request.POST['item_name']
        if not i.description:
            i.description = request.POST['description']
        i.save()
        print i.description
        return HttpResponseRedirect('/simple/')
    return render(request, 'Simpletodo/add_new.html')


def delete_item(request, pk):
    i = get_object_or_404(Item, pk=pk)
    i.delete()
    return HttpResponseRedirect('/simple/')


def update_item(request, pk):
    i = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        i.item_name = request.POST['item_name']
        if not i.description:
            i.description = request.POST['description']
        i.save()

        return HttpResponseRedirect('/simple/')
    context = {'i': i}
    return render(request, "Simpletodo/update_item.html", context=context)


def tofinish_item(pk):
    i = get_object_or_404(Item, pk=pk)
    if not i.flag:
        i.flag = True
        i.save()
    return HttpResponseRedirect('/simple/')


def notfinish_item(request, pk):
    i = get_object_or_404(Item, pk=pk)
    if i.flag:
        i.flag = False
        i.save()
    return HttpResponseRedirect('/simple/')
