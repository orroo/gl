from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views
urlpatterns = [
    #path('list/', views.avis_list, name='avis_list'),
    path('create/', views.avis_create, name='avis_create'),
    path('update/<int:pk>/', views.avis_update, name='avis_update'),
    path('delete/<int:pk>/', views.avis_delete, name='avis_delete'),
    path('approve/', views.avis_approval, name='avis_approval'),  # Approve page
    path('approve/<int:pk>/', views.approve_avis, name='approve_avis'),  # Approve individual avis
    path('avis/', views.avis_list, name='avis_list'),  
    path('disapprove/<int:pk>/', views.disapprove_avis, name='disapprove_avis'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
