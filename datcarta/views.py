from multiprocessing import context
from django.shortcuts import render
from datcarta.models import Datcarta
from datcarta.forms import new_user

def crear_datos(request):
    
   if request.method == "POST":
    pass
    #New_Usuario = Datcarta.objects.create(
        #name= "Julian Ospina Rendon",
        #cedula="1036734255",
        #Fecha_de_Ingreso = "15 agosto 2022",
        #Cargo = "Developer",
        #Salario = "2.500.000" ,
        #Tipo_de_contrato = "termino fijo"   
        #)
    #context = {
     #   "New_Usuario" : New_Usuario
    #}
   elif request.method == "GET":
     form = new_user()
     context = {'form':form}
    
     return render(request,"New_Usuario.html", context=context)




