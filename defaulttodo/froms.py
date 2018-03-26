#coding:utf-8
from django import forms
from .models import Item,User,Biu

class UserForm(forms.ModelForm):
    user_pass =forms.CharField(max_length=120,widget=forms.PasswordInput())
    class Meta:
        model = User
        fields =('user_name','user_pass')
class ItemForm(forms.ModelForm):

    item_name = forms.CharField(max_length=120,help_text='你必须输入这个笨蛋')
    item_description = forms.CharField(max_length=120,required=False)
    flag = forms.BooleanField(widget=forms.HiddenInput(),initial=False)
    pub_tiem = forms.DateTimeField(widget=forms.HiddenInput())
    proiorty = forms.IntegerField(max_value=10)
    class Mata:
        model = Item
        fields = ('item_name','item_description','priority')

class BiuForm(forms.ModelForm):
    class Meta:
        model = Biu
        fields = ('biu',)