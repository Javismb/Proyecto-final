from django.db import models

class Datcarta(models.Model):
    
    name = models.CharField(max_length=50)
    Cedula = models.Float()
    Fecha_de_Ingreso = models.date()
    Cargo = models.CharField(max_length=50)
    Salario = models.FloatField() 
    Tipo_de_contrato = models.CharField(max_length=50)   
    is_active = models.BooleanField() 