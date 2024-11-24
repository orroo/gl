from django.contrib.auth.backends import BaseBackend
from .models import user
from django.core.exceptions import ValidationError

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            userc = user.objects.get(mail=username)  # Authenticate using email instead of username
            if userc.check_password(password):
                
                return userc
            else :
                raise ValidationError("password is incorrect")
        except user.DoesNotExist:
            ValidationError("mail is incorrect")
            return None
