from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('', include('users.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]