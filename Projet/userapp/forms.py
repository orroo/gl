from django import forms
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from django.shortcuts import redirect
from .backends import EmailBackend


class uform (UserCreationForm):
    class Meta:
        model = user
        fields = ['cin','nom','prenom','num_tel','adresse','mail','date_naissance','username','role','password1','password2']

    
    date_naissance=forms.DateField(label="Date de naissanace",widget=forms.DateInput(attrs={'type' : 'date'}))
    def __init__(self, *args, **kwargs):
        super(uform, self).__init__(*args, **kwargs)
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


# class userform(forms.ModelForm):
#     class Meta:
#         model = user
#         fields = ['cin','nom','prenom','num_tel','adresse','mail','date_naissance','username','role','password1','password2']

#     date_naissance=forms.DateField(label="Date de naissanace",widget=forms.DateInput(attrs={'type' : 'date'}))
#     password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'type' : 'password'}))
#     def __init__(self, *args, **kwargs):
#         super(userform, self).__init__(*args, **kwargs)
#         for key, value in self.fields.items():
#             value.widget.attrs['class'] = 'form-control'


#     def clean_password(self):
#         password = self.cleaned_data.get('password')
#         if len(password) < 8:
#             raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
#         return password
    

#     def clean_cin(self):
#         cin = self.cleaned_data.get('cin')
#         if len(cin) < 8:
#             raise forms.ValidationError("Le cin doit contenir au moins 8 caractères.")
#         return cin
    

#     def clean_num_tel(self):
#         num_tel = self.cleaned_data.get('num_tel')
#         if len(num_tel) < 8:
#             raise forms.ValidationError("Le numero de telephone doit contenir au moins 8 chiffres.")
#         return num_tel
    
    

#     def clean_confirm_password(self):
#         password = self.cleaned_data.get('password')
#         confirm_password = self.cleaned_data.get('confirm_password')
#         if password != confirm_password:
#             raise forms.ValidationError("Les mots de passe ne correspondent pas.")
#         return confirm_password

#     def clean_email(self):
#         email = self.cleaned_data.get('mail')
#         if user.objects.filter(email=email).exists():
#             raise forms.ValidationError("L'adresse email est déjà associée à un compte.")
#         return email

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if user.objects.filter(username=username).exists():
#             raise forms.ValidationError("Le nom d'utilisateur est déjà pris.")
#         return username

#     # Validation globale pour garantir que le mot de passe et la confirmation sont identiques
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')

#         if password and confirm_password and password != confirm_password:
#             self.add_error('confirm_password', "Les mots de passe ne correspondent pas.")
        
#         return cleaned_data




    
class upuserform(forms.ModelForm):
    class Meta:
        model = user
        fields = ['cin','nom','prenom','num_tel','adresse','mail','date_naissance','username','role','password']

    date_naissance=forms.DateField(label="Date de naissance ",widget=forms.DateInput(attrs={'type' : 'date'}))
    def __init__(self, *args, **kwargs):
        super(upuserform, self).__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'

    role=forms.CharField(widget=forms.TextInput(attrs={'readonly' :True,  'value' : 'passager'}))
    
    


    

    
class loginform(forms.ModelForm):
    class Meta:
        model = user
        fields = ['mail','password']



    password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'type' : 'password'}))
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Capture request if passed
        super().__init__(*args, **kwargs)
        for key, value in self.fields.items():
            value.widget.attrs['class'] = 'form-control'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)   
    
            # 
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('mail')
        password = cleaned_data.get('password')
        print(email)
        print(password)

        # Check if both fields are provided
        if not email :
            raise forms.ValidationError("Both mail and password are required.")

        # Authenticate the user using Django's built-in authenticate function
        # user = authenticate(mail=email , password=password)

        user = EmailBackend.authenticate(self,self.request, username=email, password=password)
        if user is None:
            raise forms.ValidationError("login failed")
        else :
            return cleaned_data
        

    def get_user(self):
        email = self.cleaned_data.get('mail')
        password = self.cleaned_data.get('password')
        # Assuming you have a User model
        try:
            userc = user.objects.get(mail=email)
            print(userc.password)
            if userc.check_password(password):
                return userc
            else:
                self.add_error('password','incorrect password')
                return redirect('home')
                # raise ValidationError("mot de passe incorrect")
            # 
        except user.DoesNotExist:
            self.add_error('mail','incorrect mail')
            return redirect('home')
        
    
    


    