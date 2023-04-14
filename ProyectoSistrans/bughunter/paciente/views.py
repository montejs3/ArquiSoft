from django.shortcuts import render
from .forms import PacienteForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.paciente_logic import create_paciente, get_pacientes

def paciente_list(request):
    pacientes = get_pacientes()
    context = {
        'pacientes_list': pacientes
    }
    return render(request, 'Paciente/paciente.html', context)

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            create_paciente(form)
            messages.add_message(request, messages.SUCCESS, 'Paciente create successful')
            return HttpResponseRedirect(reverse('pacienteCreate'))
        else:
            print(form.errors)
    else:
        form = PacienteForm()

    context = {
        'form': form,
    }

    return render(request, 'Paciente/pacienteCreate.html', context)