from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page.as_view(), name='register_page'),  # Define the URL for registration
]