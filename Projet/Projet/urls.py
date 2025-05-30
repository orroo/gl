"""
URL configuration for Projet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path , include
from .view import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',default_view, name='home'),
    path('welcome',welcome_view,name='welcome'),
    path('check',my_view,name='check'),

    path('choix',choix_view, name='choix'),
    path('choix2',choix2_view, name='choix2'),
    path('',include('avisApp.urls')),
    path('user/',include('userapp.urls')),
    path('passager/',include('passagerapp.urls')),
    path('conducteur/',include('conducteurapp.urls')),
    path('catalogue/',include('Catalogue.urls')),
    path('rides/', include('Rides.urls')),  # Match the exact app name
    path('user/', include('userapp.urls')), 
    path('stat/', include('avisApp.urls')), # Include user app URLs
   
]
