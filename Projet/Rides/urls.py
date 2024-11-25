from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.ride_list, name='ride_list'),  # List of all rides
    path('create/', views.create_ride, name='create_ride'),  # Ride creation page
    path('user/login/', auth_views.LoginView.as_view(), name='user_login'),  # Login page
    path('edit/<int:pk>/', views.edit_ride, name='edit_ride'),  # Access via /rides/edit/<pk>/
    path('delete/<int:pk>/', views.delete_ride, name='delete_ride'),  # Access via /rides/delete/<pk>/
    path('<int:pk>/', views.ride_detail, name='ride_detail'),
    path('<int:pk>/reserve/', views.reserve_ride, name='reserve_ride'),  # URL pattern for reserving a ride
    
    path('my-reservations/', views.my_reservations, name='my_reservations'),
    path('cancel/<int:pk>/', views.cancel_reservation, name='cancel_reservation'),  # New cancel reservation URL
    
    path('my_rides/', views.my_rides, name='my_rides'),
    



    
]

# Only include this part when in development to serve static files
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

