

from django.urls import path
from app_gestion_bd.views import*

urlpatterns = [

    path('inicio/', gestion_principal,name="inicio"),
    path('medicos/', vista_medicos,name="medicos"),
    path('pacientes/', vista_pacientes,name="pacientes"),
    path('usuarios_sistema/', vista_usuarios_sistema,name="usuarios"),
    path('busqueda/', vista_seccion_busquedas,name="busqueda"),
    path('guia/', vista_guia ,name="guia"),
    path('datos/', vista_datos ,name="datos"),
]
