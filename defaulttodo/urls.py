from django.conf.urls import url
from . import views

app_name = 'default'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.resgister, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    # url(r'^zanshi/$',views.zanshi,name='zanshi')
    url(r'^add_item/$', views.add_item, name='add_item'),
    url(r'^(?P<pk>[0-9]+)/item/$', views.item_detail, name='item_detail'),
    url(r'^(?P<pk>[0-9]+)/update_item/$',
        views.update_item, name='update_item'),
    url(r'^(?P<pk>[0-9]+)/tofinish_item/$',
        views.tofinish_item, name='tofinish_item'),
    url(r'^(?P<pk>[0-9]+)/notfinish_item/$',
        views.notfinish_item, name='notfinish_item'),
    url(r'^(?P<pk>[0-9]+)/delete_item/$',
        views.delete_item, name='delete_item'),

]
