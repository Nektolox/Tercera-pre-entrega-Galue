from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from DIDs.models import DID, Tarifa, Compania
# Create your views here.

def inicio(request):
    return render(request,'dids/inicio.html')

def buscarDID(request):
    
    resultado = None 
    mensaje = None 
    
    if 'numero' in request.GET: 
        
        numero = request.GET['numero'] 
        try: 
            resultado = DID.objects.get(numero=numero) 
        except DID.DoesNotExist: 
            mensaje = "El número DID no se encuentra registrado." 
            
        return render(request, 'dids/DIDsSearch.html', {'resultado': resultado, 'mensaje': mensaje})
    
    return render(request, 'dids/DIDsSearch.html')

def registrarDID(request):
    
    if request.method == "POST":  # Si el formulario fue enviado
       
        numero=DID(numero=request.POST["numero"],pais=request.POST["pais"],empresa=request.POST["empresa"],minutos_uso=request.POST["minutos_uso"])
        numero.save()

        return render(request,'dids/inicio.html')
    
    return render(request, 'dids/NewDIDs.html')

def buscarTarifa(request):
    return render(request, 'dids/PriceSearch.html')

def registrarTarifa(request):

    if request.method == "POST":  
       
        tarifa=Tarifa(trafico_entrante=request.POST["trafico_entrante"],trafico_saliente=request.POST["trafico_saliente"],precio_por_numero=request.POST["precio_por_numero"],pais=request.POST["pais"])
        tarifa.save()

        return render(request,'dids/inicio.html')
    
    return render(request, 'dids/NewPrice.html') 

def buscarCompania(request):
    return render(request, 'dids/CompanySearch.html')

def registrarCompania(request):
    
    if request.method == "POST":  
       
        compania=Compania(direccion=request.POST["direccion"],codigo_postal=request.POST["codigo_postal"],nombre=request.POST["nombre"],persona_contacto=request.POST["persona_contacto"],NOCemail=request.POST["NOCemail"])
        compania.save()

        return render(request,'dids/inicio.html')
    
    return render(request, 'dids/NewCompany.html')

