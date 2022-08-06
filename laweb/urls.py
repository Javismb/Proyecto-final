from django.contrib import admin
from django.urls import path
from laweb.views import usuarios, template_proyect

urlpatterns = [
    path('admin/', admin.site.urls),
    path("usuarios/", usuarios, name="usuarios"),
    path("template_proyect/", template_proyect, name="template_proyect")
]
