from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['name', 'description', 'departure_time', 'start_point', 'destination', 'available_seats', 'price', 'is_recurring']
        
    # Optional: Add a widget for departure_time to ensure it is rendered correctly
    departure_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
