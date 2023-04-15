from django.db import models
from doctor.models import Doctor
from paciente.models import Paciente


class Ips(models.Model):

    name = models.CharField(max_length=100)
    nit = models.FloatField(null=True, blank=True, default=None)
    sucursal = models.CharField(max_length=100,default='colina')
    paciente= models.ManyToManyField(Paciente)
    doctores= models.ManyToManyField(Doctor)
    def __str__(self):
        return '{}'.format(self.name)