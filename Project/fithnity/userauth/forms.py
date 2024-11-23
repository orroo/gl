from django import forms
from userauth.models import Userauth

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Userauth
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hache le mot de passe
        if commit:
            user.save()
        return user

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 8 caractères.")
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return confirm_password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Userauth.objects.filter(email=email).exists():
            raise forms.ValidationError("L'adresse email est déjà associée à un compte.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Userauth.objects.filter(username=username).exists():
            raise forms.ValidationError("Le nom d'utilisateur est déjà pris.")
        return username

    # Validation globale pour garantir que le mot de passe et la confirmation sont identiques
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Les mots de passe ne correspondent pas.")
        
        return cleaned_data



