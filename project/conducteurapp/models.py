from django.db import models

from userapp.models import *
# Create your models here.

class conducteur(user) :
    nb_jetons=models.IntegerField('nombre de jetons',default=0)
    assurance = models.CharField('nom d\'assurance',max_length=100 )
    vehicule=models.CharField('description du vehicule', max_length=1000)
    note=models.FloatField('note' , default=0)
    num_permis=models.CharField('numero de permis' ,max_length=12, validators=[cin_validator])
    