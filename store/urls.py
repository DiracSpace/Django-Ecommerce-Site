from django.urls import path, re_path
from . import views 

urlpatterns = [
    re_path(r'^$', views.Store, name='store'),
    re_path(r'^checkout/$', views.Checkout, name='checkout'),
    re_path(r'^cart/$', views.Cart, name='cart'),
]