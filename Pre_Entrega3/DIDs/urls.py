from django.urls import path
from DIDs import views

urlpatterns = [
    path('Inicio/', views.inicio, name="Inicio"),
    path('BuscarDIDs/', views.buscarDID, name="BusDIDs"),
    path('RegistrarDIDs/', views.registrarDID, name="RegDIDs"),
    path('BuscarTarifa/', views.buscarTarifa, name="BusTar"),
    path('BuscarComp/', views.buscarCompania, name="BusComp"),
    path('RegistrarComp/', views.registrarCompania, name="RegComp"),
]