from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
# Create your views here.

def buscarDID(request):
    return HttpResponse("Aca se buscan DIDs")

def registrarDID(request):
    return HttpResponse("Aca se registran DIDs")

def buscarTarifa(request):
    return HttpResponse("Aca se buscan Tarifas")

def registrarTarifa(request):
    return HttpResponse("Aca se registran Tarifas")

def buscarCompania(request):
    return HttpResponse("Aca se buscan Companias")

def registrarCompania(request):
    return HttpResponse("Aca se registran Companias")
