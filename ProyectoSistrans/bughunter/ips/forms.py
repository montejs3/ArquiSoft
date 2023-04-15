from django import forms
from .models import Ips

class IpsForm(forms.ModelForm):
    class Ips:
        model = Ips
        fields=[
            'name',
            'nit',
            'sucursal',

            
        ]
        labels={
            'name':'Nombre de la IPS',
            'nit':'Nit',
            'sucursal':'Sucursal',
            
            
        }