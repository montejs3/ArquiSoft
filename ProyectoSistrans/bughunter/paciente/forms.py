from django import forms
from .models import Paciente
class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields=[
            'namePaciente',
            'regimen',
            'prioridadpaciente',
            'edad',
            'estatura',
            'documento',
            #'fechaNacimiento',
        ]
        labels={
            'namePaciente':'Nombre del paciente',
            'regimen':'Regimen',
            'prioridadpaciente':'Prioridad del paciente',
            'edad':'Edad',
            'estatura':'Estatura',
            'documento':'Documento',
            #'fechaNacimiento':'Fecha de nacimiento',
        }
