from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

from django.conf import settings

# Custom validation for future dates
def validate_future_date(value):
    if value <= timezone.now():
        raise ValidationError("The date and time must be in the future.")

# Custom validation for city/town format
def validate_city_town(value):
    if not isinstance(value, str) or len(value.split(',')) != 2:
        raise ValidationError("The format must be 'town, Tunisia'.")

# Ride model
class Ride(models.Model):
    id_ride = models.IntegerField(primary_key=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)


    name = models.CharField(
        max_length=100,
        validators=[RegexValidator(regex=r'^[\w\s]+$', message="The name can only contain alphanumeric characters.")]
    )
    
    description = models.TextField(blank=True, null=True)

    departure_time = models.DateTimeField(
        validators=[validate_future_date],  # Ensure the date and time are in the future
        error_messages={'required': "The departure date and time are required."},
    )

    start_point = models.CharField(
        max_length=255,
        validators=[validate_city_town],
        error_messages={'invalid': "The start point must be 'town, Tunisia'."}
    )

    destination = models.CharField(
        max_length=255,
        validators=[validate_city_town],
        error_messages={'invalid': "The destination must be 'town, Tunisia'."}
    )

    available_seats = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(4)],  # Seats between 1 and 4
        error_messages={ 
            'min_value': "The number of available seats cannot be less than 1.",
            'max_value': "The number of available seats cannot be more than 4.",
            'invalid': "Please enter a valid number of available seats."
        }
    )

    # Price field with validation between 0 and 15 DT
    price = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        validators=[MinValueValidator(0), MaxValueValidator(15)],  # Max value updated to 15
        error_messages={
            'min_value': "The price must be greater than 0.",
            'max_value': "The price cannot be more than 15 DT.",
            'invalid': "Please enter a valid price."
        }
    )

    RECURRING_CHOICES = [
        ('ponctuel', 'Single Trip'),
        ('recurrent', 'Recurring Trip'),
    ]
    
    is_recurring = models.CharField(
        max_length=10,
        choices=RECURRING_CHOICES,
        default='ponctuel',  # Default to Single Trip
        error_messages={'invalid_choice': "Please choose between 'Single Trip' or 'Recurring Trip'."}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.start_point} to {self.destination} at {self.departure_time}"
    

    def get_is_recurring_display(self):
        return "Recurring" if self.is_recurring else "One-time" 
    def is_full(self):
        return self.available_seats == 0



class Reservation(models.Model):
    user_id = models.IntegerField(default=1)  # Replace with ForeignKey(User) if using authentication
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='reservations')
    reservation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.ride.name} by User {self.user_id} on {self.reservation_date}"
    
    