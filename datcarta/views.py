from multiprocessing import context
from django.shortcuts import render
from datcarta.models import Datcarta

def crear_datos(request):
    New_Usuario = Datcarta.objects.create(
        name= "Julian Ospina Rendon",
        cedula="1036734255",
        Fecha_de_Ingreso = "15 agosto 2022",
        Cargo = "Developer",
        Salario = "2.500.000" ,
        Tipo_de_contrato = "termino fijo"   
        )
    context = {
        "New_Usuario" : New_Usuario
    }
    return render(request,"New_Usuario.html", context=context)
    