from django import forms
from .models import *
class userform(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

    date_naissance=forms.DateField(label="Conference Start Date",widget=forms.DateInput(attrs={'type' : 'date'}))
    def __init__(self, *args, **kwargs):
        super(userform, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'



    