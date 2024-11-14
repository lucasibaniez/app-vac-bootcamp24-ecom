from rest_framework import serializers

from .models import VacunaAplicada

class VacunacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacunaAplicada
        fields = '__all__'

