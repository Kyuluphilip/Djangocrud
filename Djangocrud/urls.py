"""
URL configuration for Djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('registration.urls')),
    path('admin/', admin.site.urls),
    path('home/', include('registration.urls')),
    path('register/', include('registration.urls')),
    path('base/', include('registration.urls')),
    path('login/', include('registration.urls')),
    path('products/', include('registration.urls')),
    path('courses/', include('registration.urls')),
   # path('updates/', include('registration.urls')),
    path('dashboard/', include('registration.urls')),


]