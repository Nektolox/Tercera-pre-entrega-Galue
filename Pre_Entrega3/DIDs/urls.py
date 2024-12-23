from django.urls import path
from .views import InicioView, DIDListView, DIDCreateView, TarifaListView, TarifaCreateView, CompaniaListView, CompaniaCreateView

urlpatterns = [
    path('Inicio/', InicioView.as_view(), name="Inicio"),
    path('BuscarDIDs/', DIDListView.as_view(), name="BusDIDs"),
    path('RegistrarDIDs/', DIDCreateView.as_view(), name="RegDIDs"),
    path('BuscarTarifa/', TarifaListView.as_view(), name="BusTar"),
    path('RegistrarTarifa/', TarifaCreateView.as_view(), name="RegTar"),
    path('BuscarComp/', CompaniaListView.as_view(), name="BusComp"),
    path('RegistrarComp/', CompaniaCreateView.as_view(), name="RegComp"),
]