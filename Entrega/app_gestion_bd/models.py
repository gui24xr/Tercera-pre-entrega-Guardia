from django.db import models

# Create your models here.

#*--------------------------------------------------------------------------------------------------------

class medico(models.Model):

    lista_especialidades = [(1, "especialidad 1"), (2, "especialidad 2"),(3, "especialidad 3")]
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30, choices= lista_especialidades)
    matricula = models.IntegerField()


    def __str__(self) -> str:
        return f"Medico: {self.apellido} {self.nombre}, {self.especialidad}, Matricula numero: {self.matricula}"
    
    
#*--------------------------------------------------------------------------------------------------------

class paciente(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    obra_social = models.CharField(max_length=30)
    dni = models.IntegerField()

    def __str__(self) -> str:
        return f"Paciente: {self.apellido} {self.nombre}, DNI: {self.dni}, Obra Social: {self.obra_social}"
    
#*--------------------------------------------------------------------------------------------------------

class usuario(models.Model): #La lista de personas autotizadas que pueden utilizar el sitio.
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    dni = models.IntegerField()

    def __str__(self) -> str:
        return f"Usuario: {self.apellido} {self.nombre}, DNI: {self.dni}"

#*--------------------------------------------------------------------------------------------------------

