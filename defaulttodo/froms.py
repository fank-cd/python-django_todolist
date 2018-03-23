#coding:utf-8
from django import forms
from .models import Item

class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=120,help_text='输入名字啊傻逼')
    password =forms.CharField(max_length=120,widget=forms.PasswordInput)

class ItemForm(forms.ModelForm):
    class Mata:
        model = Item
        fields = ('item_name','item_description','priority')
