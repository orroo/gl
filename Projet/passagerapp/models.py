from django.db import models
from userapp.models import *
# Create your models here.

class passager(user) :
    nb_jetons=models.IntegerField('nombre de jetons',default=0)
    def __str__(self):
        return self.username + "(passager)"
