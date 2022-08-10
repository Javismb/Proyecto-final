from django import forms

class new_user (forms.Form):

    name = forms.CharField(max_length=40)
    Cedula = forms.FloatField()
    Cargo = forms.CharField(max_length=50)
    salario = forms.FloatField() 
    Tipo_de_contrato = forms.CharField(max_length=50)   
   