from django.views.generic import TemplateView, ListView, DetailView, CreateView 
from django.shortcuts import render 
from django.urls import reverse_lazy 
from .models import DID, Tarifa, Compania
# Create your views here.


class InicioView(TemplateView): 
    
    template_name = 'dids/inicio.html'


class DIDListView(TemplateView): 
    
    template_name = 'dids/DIDsSearch.html' 
        
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        numero = self.request.GET.get('numero') 
        if numero: 
            try: 
                context['resultado'] = DID.objects.get(numero=numero) 
            
            except DID.DoesNotExist: 
                context['mensaje'] = "The DID number is not registered yet." 
        
        return context    

class DIDCreateView(CreateView): 
    
    model = DID 
    template_name = 'dids/NewDIDs.html' 
    fields = ['numero', 'pais', 'empresa', 'minutos_uso'] 
    success_url = reverse_lazy('inicio') 
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['companias'] = Compania.objects.all().order_by('nombre') 
        return context 
        
    def form_valid(self, form): 
        form.instance.empresa = self.request.POST["empresa"] 
        return super().form_valid(form)

class TarifaListView(TemplateView): 
        
    template_name = 'dids/PriceSearch.html' 
        
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        pais = self.request.GET.get('pais') 
            
        if pais: 
            try: 
                context['resultado'] = Tarifa.objects.get(pais=pais) 
            except Tarifa.DoesNotExist: 
                context['mensaje'] = "We currently don't have a price for the requested country" 
            
        return context

class TarifaCreateView(CreateView): 
    
    model = Tarifa 
    template_name = 'dids/NewPrice.html' 
    fields = ['trafico_entrante', 'trafico_saliente', 'precio_por_numero', 'pais'] 
    success_url = reverse_lazy('inicio')

class CompaniaListView(TemplateView): 
    
    template_name = 'dids/CompanySearch.html' 
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        nombre = self.request.GET.get('nombre') 
        
        if nombre: 
            try: 
                context['resultado'] = Compania.objects.get(nombre=nombre) 
            except Compania.DoesNotExist: 
                context['mensaje'] = "This company is not registered yet." 
        
        return context

class CompaniaCreateView(CreateView): 
    
    model = Compania 
    template_name = 'dids/NewCompany.html' 
    fields = ['direccion', 'codigo_postal', 'nombre', 'persona_contacto', 'NOCemail'] 
    success_url = reverse_lazy('inicio')