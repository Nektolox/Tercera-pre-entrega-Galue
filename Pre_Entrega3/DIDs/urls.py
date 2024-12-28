from django.urls import path
from .views import InicioView, DIDListView, DIDCreateView, TarifaListView, TarifaCreateView, CompaniaListView, CompaniaCreateView, DIDCompanySearchView, DIDUpdateView, DIDDeleteView

urlpatterns = [
    path('Inicio/', InicioView.as_view(), name="Inicio"),
    path('BuscarDIDs/', DIDListView.as_view(), name="BusDIDs"),
    path('RegistrarDIDs/', DIDCreateView.as_view(), name="RegDIDs"),
    path('BuscarTarifa/', TarifaListView.as_view(), name="BusTar"),
    path('RegistrarTarifa/', TarifaCreateView.as_view(), name="RegTar"),
    path('BuscarComp/', CompaniaListView.as_view(), name="BusComp"),
    path('RegistrarComp/', CompaniaCreateView.as_view(), name="RegComp"),
    path('UD_DIDs/', DIDCompanySearchView.as_view(), name='BusDIDsByCompany'),
    path('UpdateDIDs/<int:pk>/', DIDUpdateView.as_view(), name='UpdateDID'),
    path('DeleteDIDs/<int:pk>/', DIDDeleteView.as_view(), name='DeleteDID'),
]



