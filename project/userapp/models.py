from django.db import models
import re
from django.core.validators import ValidationError , RegexValidator
# Create your models here.

def email_validator(value):
    if( not value.endswith("@esprit.tn")) and (not value.endswith("@gmail.com")):
        raise ValidationError("invalid email")


def cin_validator(value):
    RegexValidator(
        regex=r'^\d{8}$',
        message='must contain 8 numbers'
    )
    

class user (models.Model):
    cin= models.CharField(('CIN') , max_length=8 , primary_key=True,validators=[cin_validator])
    nom =  models.CharField(('nom') , max_length=150)
    prenom=models.CharField(('prenom') , max_length=150)
    num_tel=models.CharField(('numbero de telephone') , max_length=150)
    adresse= models.CharField(('adresse') , max_length=150)
    mail= models.CharField(('mail') , max_length=150,validators=[email_validator])
    date_naissance=models.DateField(('date de naissance'))
    username= models.CharField(('username') , max_length=150,unique=True)
    mot_de_passe= models.CharField(('mot de passe') , max_length=150)
    role= models.CharField(('role') , max_length=150)
    def __str__(self):
        return self.username
    

