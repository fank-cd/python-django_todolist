from django.conf.urls import url
from . import views

app_name = 'advance'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^add_item/$', views.add_item, name='add_item'),
    url(r'list/$', views.list, name='list'),
    url(r'^(?P<pk>[0-9]+)/item/$', views.item_detail, name='item_detail'),
    url(r'^(?P<pk>[0-9]+)/to_done/$', views.to_done, name='to_done'),
    url(r'^(?P<pk>[0-9]+)/not_done/$', views.not_done, name='not_done'),
    url(r'^(?P<pk>[0-9]+)/to_delete/$', views.to_delete, name='to_delete'),
    url(r'^(?P<pk>[0-9]+)/update_item/$', views.update_item, name='update_item'),
]
