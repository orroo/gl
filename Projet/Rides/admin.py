from django.contrib import admin

# Register your models here.
from .models import Ride,Reservation  # Import your models

# Register your models with the admin interface
admin.site.register(Ride)
admin.site.register(Reservation)