from django.urls import path
from DIDs import views

urlpatterns = [
    path('BuscarDIDs/', views.buscarDID),
    path('RegistrarDIDs/', views.registrarDID),
    path('BuscarTarifa/', views.buscarTarifa),
    path('RegistrarTarifa/', views.registrarTarifa),
    path('BuscarComp/', views.buscarCompania),
    path('RegistrarComp/', views.registrarCompania),
]