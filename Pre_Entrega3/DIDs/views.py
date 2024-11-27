from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from DIDs.models import DID
# Create your views here.

def inicio(request):
    return render(request,'dids/inicio.html')

def buscarDID(request):
    return render(request, 'dids/DIDsSearch.html')

def registrarDID(request):
    
    if request.method == "POST":  # Si el formulario fue enviado
       
        numero=DID(numero=request.POST["numero"],pais=request.POST["pais"],empresa=request.POST["empresa"],minutos_uso=request.POST["minutos_uso"])
        numero.save()

        return render(request,'DIDs/inicio.html')
    
    return render(request, 'DIDs/NewDIDs.html')

def buscarTarifa(request):
    return render(request, 'dids/PriceSearch.html')

def registrarTarifa(request):
    return render(request, 'dids/NewPrice.html')

def buscarCompania(request):
    return render(request, 'dids/CompanySearch.html')

def registrarCompania(request):
    return render(request, 'dids/NewCompany.html')
