from django import forms
from .models import *



from django.contrib.auth.forms import UserCreationForm


class pform (UserCreationForm):
    class Meta:
        model = passager
        fields = ['cin','nom','prenom','num_tel','adresse','mail','date_naissance','username','role','password1','password2']


    date_naissance=forms.DateField(label="Date de naissanace",widget=forms.DateInput(attrs={'type' : 'date'}))
    
    role=forms.CharField(widget=forms.TextInput(attrs={'readonly' :True,  'value' : 'passager'}))
        
    def __init__(self, *args, **kwargs):
        super(pform, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'


    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return password
    

    def clean_cin(self):
        cin = self.cleaned_data.get('cin')
        if len(cin) < 8:
            raise forms.ValidationError("Le cin doit contenir au moins 8 caractères.")
        return cin
    

    def clean_num_tel(self):
        num_tel = self.cleaned_data.get('num_tel')
        if len(num_tel) < 8:
            raise forms.ValidationError("Le numero de telephone doit contenir au moins 8 chiffres.")
        return num_tel
    

    def clean_email(self):
        email = self.cleaned_data.get('mail')
        if user.objects.filter(email=email).exists():
            raise forms.ValidationError("L'adresse email est déjà associée à un compte.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if user.objects.filter(username=username).exists():
            raise forms.ValidationError("Le nom d'utilisateur est déjà pris.")
        return username


class passagerform(forms.ModelForm):
    class Meta:
        model = passager
        fields = ['cin','nom','prenom','num_tel','adresse','mail','date_naissance','username','role','password']

    date_naissance=forms.DateField(label="Date de naissance",widget=forms.DateInput(attrs={'type' : 'date'}))
    def __init__(self, *args, **kwargs):
        super(passagerform, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'

    role=forms.CharField(widget=forms.TextInput(attrs={'readonly' :True,  'value' : 'passager'}))
    
    


    