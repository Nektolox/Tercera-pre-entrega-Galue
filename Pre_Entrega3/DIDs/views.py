from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request,'dids/inicio.html')

def buscarDID(request):
    return render(request, 'dids/DIDsSearch.html')

def registrarDID(request):
    return render(request, 'dids/NewDIDs.html')

def buscarTarifa(request):
    return render(request, 'dids/PriceSearch.html')

def registrarTarifa(request):
    return render(request, 'dids/NewPrice.html')

def buscarCompania(request):
    return render(request, 'dids/CompanySearch.html')

def registrarCompania(request):
    return render(request, 'dids/NewCompany.html')
