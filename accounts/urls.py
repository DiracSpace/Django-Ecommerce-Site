from django.conf.urls import url
from django.urls import path, re_path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/$', views.usersignup, name='signup'),
    re_path(r'^login/$', views.userlogin, name='login'),
    re_path(r'^logout/$', views.userlogout, name='logout'),
]