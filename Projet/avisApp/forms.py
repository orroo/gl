from django import forms
from .models import Avis

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ['rating', 'comment']  # Exclude 'author' and 'recipient'
        widgets = {
            'rating': forms.Select(choices=Avis.RATING_CHOICES, attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }

