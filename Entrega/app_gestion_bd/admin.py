from django.contrib import admin
from app_gestion_bd.models import usuario, medico, paciente

# Register your models here.

admin.site.register(usuario)
admin.site.register(medico)
admin.site.register(paciente)