from django.http import HttpResponse
from django.shortcuts import render



def usuarios(request):
    return HttpResponse("Crear usuario y contraseña")

def template_proyect(request):
    return render(request, "templates.html", context={})

def formulario(request):
    return render(request, "formulario_1.html", context={})

def new_user(request):
    return render (request, "New_Usuario.html", context={})    
