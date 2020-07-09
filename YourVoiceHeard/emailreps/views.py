from django.shortcuts import render
from .models import Senator, Representative, Issue

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def blm(request):
    context = {}
    return render(request, 'blm.html', context)

def ice(request):
    context = {}
    return render(request, 'ice.html', context)

def yemen(request):
    context = {}
    return render(request, 'yemen.html', context)

def climatechange(request):
    context = {}
    return render(request, 'climatechange.html', context)

def proposeissues(request):
    context = {}
    return render(request, 'proposeissues.html', context)




