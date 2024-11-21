from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('',my_view),
    path('*',my_view_404),
    path('about/',my_view_about),
    path('blog/',my_view_blog),
    path('cars/',my_view_cars),
    path('contact/',my_view_contact),
    path('feature/',my_view_feature),
    path('service/',my_view_service),
    path('team/',my_view_team),
    path('testimonial/',my_view_testimonial),
    path('form/',my_view_form),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
