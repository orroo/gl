# avis/forms.py
from django import forms
from .models import Avis
from Rides.models import Ride

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['rating', 'comment', 'ride']  # Add 'ride' to the fields
        widgets = {
            'rating': forms.Select(choices=Avis.RATING_CHOICES, attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            'ride': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for rides
        }

