from multiprocessing import context
from django.shortcuts import render,redirect
from datcarta.models import Datcarta
from datcarta.forms import new_user

def crear_datos(request):
    
   if request.method == "POST":
    
    form = new_user(request.POST)

    if form.is_valid():

     Datcarta.objects.create(
        name= form.cleaned_data('name'),
        cedula = form.cleaned_data('cedula'),
        Fecha_de_Ingreso = form.cleaned_data('Fecha_de_ingreso'),
        Cargo = form.cleaned_data('Cargo'),
        Salario = form.cleaned_data('Salario'),
        Tipo_de_contrato = form.cleaned_data('Tipo_de_contrato ')  
      )

     return redirect(usuarios)
    
    
   elif request.method == "GET":
     form = new_user()
     context = {'form':form}
    
     return render(request,"New_Usuario.html", context=context)




