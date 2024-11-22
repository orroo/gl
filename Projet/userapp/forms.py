from django import forms
from .models import *
class userform(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

    date_naissance=forms.DateField(label="Date de naissanace",widget=forms.DateInput(attrs={'type' : 'date'}))
    def __init__(self, *args, **kwargs):
        super(userform, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'



    
class upuserform(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'

    date_naissance=forms.DateField(label="Date de naissance ",widget=forms.DateInput(attrs={'type' : 'date'}))
    def __init__(self, *args, **kwargs):
        super(upuserform, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'

    role=forms.CharField(widget=forms.TextInput(attrs={'readonly' :True,  'value' : 'passager'}))
    
    


    