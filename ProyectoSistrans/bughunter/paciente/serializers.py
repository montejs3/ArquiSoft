from rest_framework import serializers
from . import models


class PacienteSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'namePaciente', 'regimen', 'prioridadpaciente', 'edad', 'estatura', 'documento', 'fechaNacimiento')
        model = models.Paciente