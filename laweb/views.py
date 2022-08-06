from django.http import HttpResponse
from django.shortcuts import render

def usuarios(request):
    return HttpResponse("Crear usuario y contraseña")

def template_proyect(request):
    return render(request, "templates.html", context={})
