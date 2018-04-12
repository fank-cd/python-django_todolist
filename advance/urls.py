from django.conf.urls import url
from . import views

app_name = 'advance'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^logout/$',views.user_logout,name='user_logout'),
    url(r'^add_item/$', views.add_item, name='add_item'),
    url(r'list/$',views.list,name='list')
]
