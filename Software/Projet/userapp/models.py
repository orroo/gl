from django.db import models
import re
from django.contrib.auth.models import AbstractUser
from django.core.validators import ValidationError , RegexValidator
# Create your models here.
from django.contrib.auth.hashers import make_password , check_password

def email_validator(value):
    if( not value.endswith("@esprit.tn")) :
        raise ValidationError("invalid email")


def cin_validator(value):
    RegexValidator(
        regex=r'^\d{8}$',
        message='must contain 8 numbers'
    )
    

def validate_address(value):
    # Expression régulière qui vérifie qu'il y a au moins une lettre et un chiffre
    if not re.search(r'[a-zA-Z]', value):  # Vérifier qu'il y a au moins une lettre
        raise ValidationError('L\'adresse doit contenir au moins une lettre.')
    if not re.search(r'\d', value):  # Vérifier qu'il y a au moins un chiffre
        raise ValidationError('L\'adresse doit contenir au moins un chiffre.')

class user (AbstractUser):
    cin= models.CharField(('CIN') , max_length=8 ,validators=[cin_validator])
    nom =  models.CharField(('nom') , max_length=150)
    prenom=models.CharField(('prenom') , max_length=150)
    num_tel=models.CharField(('numbero de telephone') , max_length=8 , validators=[cin_validator])
    adresse= models.CharField(('adresse') , max_length=150 , validators=[validate_address])
    mail= models.CharField(('mail') , max_length=150,validators=[email_validator])
    date_naissance=models.DateField(('date de naissance'),null=True,blank=True)
    username= models.CharField(('username') , max_length=150,unique=True)
    role= models.CharField(('role') , max_length=150)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['mail']
    def __str__(self):
        return self.username
    