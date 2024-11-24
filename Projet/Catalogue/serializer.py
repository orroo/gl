from rest_framework import serializers
from .models import *

class OffreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offre
        fields = '__all__'  # Include all fields