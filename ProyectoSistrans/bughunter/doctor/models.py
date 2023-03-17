from django.db import models
from paciente.models import Paciente
from ips.models import Ips

class Doctor(models.Model):

    nameDoctor = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100,default='general')
    consultorio = models.CharField(max_length=100,default='ml-101')
    
    paciente= models.ManyToManyField(Paciente)
    ips= models.ForeignKey(Ips, on_delete=models.CASCADE,default=None)


    def __str__(self):
        return '%s' % (self.nameDoctor)



