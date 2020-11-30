from django.urls import path, re_path, include
from . import views

app_name = 'coronas'

urlpatterns = [
    re_path(r'^$', views.Store, name='store'),
    re_path(r'^checkout/$', views.Checkout, name='checkout'),
    re_path(r'^cart/$', views.Cart, name='cart'),
    re_path(r'^update_item/$', views.updateItem, name='update'),
    re_path(r'^process_order/$', views.processOrder, name='payment'),
]