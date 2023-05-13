from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import IpsForm
from .logic.ips_logic import get_ipss, create_ips
from django.contrib.auth.decorators import login_required
from bughunter.auth0backend import getRole

@login_required
def ips_list(request):
    role = getRole(request)
    if role == 'Administrador Sistema':
        ipss = get_ipss()
        context = {
            'ipss_list': ipss
        }
        return render(request, 'Ips/ips.html', context)
    else :
        return HttpResponse('Unauthorized User')

@login_required
def ips_create(request):
    role = getRole(request)
    if role == 'Administrador Sistema':
        if request.method == 'POST':
            form = IpsForm(request.POST)
            if form.is_valid():
                create_ips(form)
                messages.add_message(request, messages.SUCCESS, 'Ips create successful')
                return HttpResponseRedirect(reverse('ipsCreate'))
            else:
                print(form.errors)
        else:
            form = IpsForm()

        context = {
            'form': form,
        }

        return render(request, 'Ips/ipsCreate.html', context)
    else :
        return HttpResponse('Unauthorized User')
