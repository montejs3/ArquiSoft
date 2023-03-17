from django.db import models


class Paciente(models.Model):


    namePaciente = models.CharField(max_length=100)
    regimen = models.CharField(max_length=100, null=True)
    prioridadpaciente = models.CharField(max_length=101,default='baja')

    edad = models.FloatField(null=True, blank=True, default=None)
    estatura = models.FloatField(null=True, blank=True, default=None)
    documento = models.FloatField(null=True, blank=True, default=None)

    fechaNacimiento = models.DateTimeField(auto_now_add=True)


 


    


    
    
    def __str__(self):
        return '{}'.format(self.namePaciente)
# Create your models here.
