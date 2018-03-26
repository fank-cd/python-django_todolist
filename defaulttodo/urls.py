from django.conf.urls import url
from . import views

app_name = 'default'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^register/$', views.resgister, name='register'),
    url(r'^zanshi/$',views.zanshi,name='zanshi')
]