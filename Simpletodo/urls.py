from django.conf.urls import url
from . import views

app_name = 'simple'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_new/$', views.add_new, name='add_new'),
    url(r'^(?P<pk>[0-9]+)/delete_item/$', views.delete_item, name='delete_item'),
    url(r'^(?P<pk>[0-9]+)/update_item/$', views.update_item, name='update_item'),
    url(r'^(?P<pk>[0-9]+)/tofinish_item/$', views.tofinish_item, name='tofinish_item'),
    url(r'^(?P<pk>[0-9]+)/notfinish_item/$', views.notfinish_item, name='notfinish_item'),
]
