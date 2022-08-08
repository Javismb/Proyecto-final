from django.contrib import admin
from django.urls import path
from laweb.views import usuarios, template_proyect, formulario, new_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path("usuarios/", usuarios, name="usuarios"),
    path("template_proyect/", template_proyect, name="template_proyect"),
    path("formulario_1/", formulario, name="formulario_1"),
    path("New_Usuario/", new_user, name="New_Usuario")
]
