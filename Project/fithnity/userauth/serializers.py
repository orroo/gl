from rest_framework import serializers
from .models import Userauth

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userauth
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'birth_date', 'address', 'role', 'carModel', 'licensePlate', 'password']  # Ajoutez 'password'

    def create(self, validated_data):
        password = validated_data.pop('password')  # Retirer le mot de passe du dict
        user = Userauth(**validated_data)
        user.set_password(password)  # Hash le mot de passe
        user.save()
        return user
