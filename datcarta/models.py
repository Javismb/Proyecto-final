from django.db import models

class Datcarta(models.Model):
    
    name = models.CharField(max_length=50)
    Cedula = models.FloatField()
    Fecha_de_Ingreso = models.CharField(max_length=50)
    Cargo = models.CharField(max_length=50)
    Salario = models.FloatField() 
    Tipo_de_contrato = models.CharField(max_length=50)   
    is_active = models.BooleanField() 