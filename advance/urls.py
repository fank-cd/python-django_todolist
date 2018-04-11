from django.conf.urls import url
from . import views

app_name = 'advance'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',views.user_login,name='user_login'),
]
