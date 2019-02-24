
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('home.urls')),
    path('app01/', include('app01.urls')),
    path('app02/', include('app02.urls')),
    path('app03/', include('app03.urls')),
    path('city/', include('city.urls')),
    path('admin/', admin.site.urls),
]
