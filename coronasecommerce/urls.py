from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="adminpanel"),
    re_path('', include('store.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)