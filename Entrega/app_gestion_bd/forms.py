from django import forms
from app_gestion_bd.tablas_de_valores import lista_especialidades,lista_obras_sociales

"""
class form_medico(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.CharField(max_length=30)
    matricula = forms.IntegerField()
  
"""

class form_medico(forms.Form):

   
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    especialidad = forms.ChoiceField(choices=lista_especialidades)
    matricula = forms.IntegerField()
    


class form_paciente(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    obra_social = forms.ChoiceField(choices=lista_obras_sociales)
    dni = forms.IntegerField()

class form_usuario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()


class form_busqueda_medico(forms.Form):
    apellido_medico = forms.CharField(max_length=30,label="APELLIDO MEDICO")
   
class form_busqueda_paciente(forms.Form):
    apellido_paciente = forms.CharField(max_length=30,label="APELLIDO PACIENTE")
    

class form_busqueda_usuario(forms.Form):
    apellido_usuario = forms.CharField(max_length=30,label="APELLIDO USUARIO")


