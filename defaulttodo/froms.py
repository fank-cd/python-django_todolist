# coding:utf-8
from django import forms
from .models import Item, Biu
from django.contrib.auth.models import User


class UserForm (forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:

        model = User
        fields = ('username', 'email', 'password')


class ItemForm (forms.ModelForm):

    item_name = forms.CharField(max_length=120, label='Item name')
    item_description = forms.CharField(max_length=120, required=False)
    priority = forms.IntegerField(max_value=10,
                                  min_value=0)  # widget=forms.TextInput()
    flag = forms.BooleanField(widget=forms.HiddenInput(), required=False)

    class Meta:

        model = Item
        fields = ('item_name', 'item_description', 'priority')


class BiuForm (forms.ModelForm):
    class Meta:

        model = Biu
        fields = ('biu',)
