from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import IpsForm
from .logic.ips_logic import get_ipss, create_ips

def ips_list(request):
    ipss = get_ipss()
    context = {
        'ipss_list': ipss
    }
    return render(request, 'Ips/ips.html', context)

def ips_create(request):
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
