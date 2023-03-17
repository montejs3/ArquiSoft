from django.db import models

from paciente.models import Paciente

class HistoriaMedica(models.Model):

    fechaConsulta = models.DateTimeField(auto_now_add=True)
    sintoma = models.CharField(max_length=100)
    sangre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    paciente= models.OneToOneField(Paciente,on_delete=models.CASCADE,primary_key=True)
    

    def __str__(self):
        return '{}'.format(self.paciente)