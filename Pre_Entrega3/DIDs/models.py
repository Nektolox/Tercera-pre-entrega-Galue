from django.db import models

# Create your models here.

class DID(models.Model):
    numero = models.CharField(max_length=15)
    pais = models.CharField(max_length=30)
    empresa = models.CharField(max_length=30)
    minutos_uso = models.IntegerField()

class Tarifa(models.Model):
    trafico_entrante = models.DecimalField(max_digits=6, decimal_places=4)
    trafico_saliente = models.DecimalField(max_digits=6, decimal_places=4)
    precio_por_numero = models.DecimalField(max_digits=6, decimal_places=4)

class Compania(models.Model):
    direccion = models.CharField(max_length=60)
    codigo_postal = models.IntegerField()
    nombre = models.CharField(max_length=60)
    persona_contacto = models.CharField(max_length=60)
    NOCemail = models.EmailField()