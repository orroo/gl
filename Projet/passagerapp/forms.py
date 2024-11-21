from django import forms
from .models import *
class passagerform(forms.ModelForm):
    class Meta:
        model = passager
        fields = '__all__'
        exclude=('nb_jetons',)

    date_naissance=forms.DateField(label="Conference Start Date",widget=forms.DateInput(attrs={'type' : 'date'}))
    def __init__(self, *args, **kwargs):
        super(passagerform, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'

    role=forms.CharField(widget=forms.TextInput(attrs={'readonly' :True,  'value' : 'passager'}))
    
    


    