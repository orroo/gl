from django import forms
from .models import *
class conducteurform(forms.ModelForm):
    class Meta:
        model = conducteur
        fields = '__all__'
        exclude=('nb_jetons','note')

    date_naissance=forms.DateField(label="Conference Start Date",widget=forms.DateInput(attrs={'type' : 'date'}))
    def __init__(self, *args, **kwargs):
        super(conducteurform, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'

    role=forms.CharField(widget=forms.TextInput(attrs={'readonly' :True,  'value' : 'conducteur'}))
    
    


    