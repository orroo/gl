from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['name', 'description', 'departure_time', 'start_point', 'destination', 'available_seats', 'price', 'is_recurring']
        

    
    def __init__(self, *args, **kwargs):
        super(RideForm, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'
    # Optional: Add a widget for departure_time to ensure it is rendered correctly
    departure_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )
