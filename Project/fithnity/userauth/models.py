from django.contrib.auth.models import AbstractUser
from django.db import models

class Userauth(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=20, unique=True)

    # Utiliser l'username comme identifiant principal
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']  # Email est requis à l'inscription

    def __str__(self):
        return self.username

