from django.urls import path
from . import views 
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
 path('paciente/', views.paciente_list),
    path('pacientecreate/', csrf_exempt(views.paciente_create), name='pacienteCreate'),
]