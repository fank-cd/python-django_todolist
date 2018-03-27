from django.conf.urls import url
from . import views

app_name = 'default'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^register/$', views.resgister, name='register'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    #url(r'^zanshi/$',views.zanshi,name='zanshi')
]