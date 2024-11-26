from django.db import models

from userapp.models import *
# Create your models here.


def validate_assurance(value):
    # Expression régulière qui vérifie qu'il y a au moins une lettre et un chiffre
    if not re.search(r'[a-zA-Z]', value):  # Vérifier qu'il y a au moins une lettre
        raise ValidationError('L\'adresse doit contenir au moins une lettre.')
    if  re.search(r'\d', value):  # Vérifier qu'il y a au moins un chiffre
        raise ValidationError('L\'adresse ne doit contenir aucun chiffre.')
    
def validate_vehicule(value):
    # Expression régulière qui vérifie qu'il y a au moins une lettre et un chiffre
    if not re.search(r'[a-zA-Z]', value):  # Vérifier qu'il y a au moins une lettre
        raise ValidationError('L\'adresse doit contenir au moins une lettre.')
   
    

def permis_validator(value):
    RegexValidator(
        regex=r'^\d{10}$',
        message='must contain 8 numbers'
    )
    


class conducteur(user) :
    nb_jetons=models.IntegerField('nombre de jetons',default=0)
    assurance = models.CharField('nom d\'assurance',max_length=100 ,validators=[validate_assurance])
    vehicule=models.CharField('description du vehicule', max_length=1000,validators=[validate_vehicule])
    note=models.FloatField('note' , default=0)
    num_permis=models.CharField('numero de permis' ,max_length=12, validators=[permis_validator])
    def __str__(self):
        return self.username + "(conducteur)"
    def is_c(self):
        return self.premium_since is not None
    