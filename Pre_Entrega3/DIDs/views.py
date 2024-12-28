from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy 
from .models import DID, Tarifa, Compania
# Create your views here.


class InicioView(TemplateView): 
    
    template_name = 'DIDs/Inicio.html'


class DIDListView(TemplateView): 
    
    template_name = 'DIDs/DIDsSearch.html' 
        
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
    template_name = 'DIDs/NewDIDs.html' 
    fields = ['numero', 'pais', 'empresa', 'minutos_uso'] 
    success_url = reverse_lazy('Inicio') 
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['companias'] = Compania.objects.all().order_by('nombre') 
        return context 
        
    def form_valid(self, form): 
        form.instance.empresa = self.request.POST["empresa"] 
        return super().form_valid(form)
    

class DIDCompanySearchView(TemplateView):
    template_name = 'DIDs/UD_DIDs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companias'] = Compania.objects.all().order_by('nombre')
        
        empresa = self.request.GET.get('empresa')
        if empresa:
            context['dids'] = DID.objects.filter(empresa=empresa)
        
        return context

class DIDUpdateView(UpdateView):
    model = DID
    template_name = 'DIDs/UpdateDIDs.html'
    fields = ['empresa', 'minutos_uso']
    success_url = reverse_lazy('BusDIDsByCompany')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companias'] = Compania.objects.all().order_by('nombre')
        return context

class DIDDeleteView(DeleteView):
    model = DID
    template_name = 'DIDs/DeleteDIDs.html'
    success_url = reverse_lazy('BusDIDsByCompany')


class TarifaListView(TemplateView): 
        
    template_name = 'DIDs/PriceSearch.html' 
        
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
    template_name = 'DIDs/NewPrice.html' 
    fields = ['trafico_entrante', 'trafico_saliente', 'precio_por_numero', 'pais'] 
    success_url = reverse_lazy('Inicio')

class CompaniaListView(TemplateView): 
    
    template_name = 'DIDs/CompanySearch.html' 
    
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
    template_name = 'DIDs/NewCompany.html' 
    fields = ['direccion', 'codigo_postal', 'nombre', 'persona_contacto', 'NOCemail'] 
    success_url = reverse_lazy('Inicio')