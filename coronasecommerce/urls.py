from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="adminpanel"),
    re_path('', include('store.urls')),
    
]
