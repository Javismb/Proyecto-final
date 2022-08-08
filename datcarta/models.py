from django.db import models

class Datcarta(models.Model):
    
    name = models.CharField(max_length=50)
    Cedula = models.FloatField()
    Fecha_de_Ingreso = models.DateField(auto_now_add=True)
    Cargo = models.CharField(max_length=50)
    salario = models.FloatField() 
    Tipo_de_contrato = models.CharField(max_length=50)   
    is_active = models.BooleanField() 

#class Carta_recomendacion(models.Model):
    
    #name = models.CharField(max_length=20)
    #cargo = models.CharField(max_length=20)
    
#class Curriculum_vitae(models.Model):

    #name = models.CharField(max_length=20)
    #salario_pretendido = models.IntegerField()
    #cargo = models.Charfield(max_lenght=20)