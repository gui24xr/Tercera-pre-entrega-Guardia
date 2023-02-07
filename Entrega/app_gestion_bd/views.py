from django.shortcuts import render
from app_gestion_bd.models import*
from app_gestion_bd.forms import*
from django.template import Template,Context

from app_gestion_bd.tablas_de_valores import get_nombre_especialidad,get_nombre_obra_social,tabla_codigos_html



# Create your views here.


def gestion_principal(request):  # Este va a ir al views del proyecto ppal

    
    return render(request,'app_gestion_bd/inicio.html')


    

def vista_medicos(request):

    if request.method == 'POST':

        formulario = form_medico(request.POST) #Creo un formulario medico que recibira un request.
        
        if formulario.is_valid():
            
            info_medico = formulario.cleaned_data  #Agarro la informacion devuelta en un diccionario?
            
            
            instancia_medico_1 = medico(nombre= info_medico['nombre'],
                                        apellido= info_medico['apellido'],
                                        especialidad= get_nombre_especialidad(int(info_medico['especialidad'])),
                                        matricula = info_medico['matricula'])
            
           
            instancia_medico_1.save()  # Guardo a la base de datos.
            mensaje = f"El medico {instancia_medico_1.apellido} fue guardado con exito en nuestra base de datos. "
          
            # Guarde el nuevo item a la base de datos, ahora aviso por medio de la pagina y pongo el boton limpiar.
            return render(request,'app_gestion_bd/medicos.html',{"formulario": formulario,"mensaje": mensaje,"boton_limpiar": True })

    
    else: # si metodo es get
        formulario = form_medico()
        return render(request,'app_gestion_bd/medicos.html',{"formulario": formulario})

        
    
    
   
def vista_pacientes(request):

    if request.method == 'POST':

        formulario = form_paciente(request.POST) #Creo un formulario medico que recibira un request.
        
        if formulario.is_valid():
            
            info_paciente = formulario.cleaned_data  #Agarro la informacion devuelta en un diccionario?
            
            instancia_paciente_1 = paciente(nombre= info_paciente['nombre'],
                                    apellido= info_paciente['apellido'],
                                    obra_social= get_nombre_obra_social(int(info_paciente['obra_social'])),
                                    dni = info_paciente['dni'])
            instancia_paciente_1.save()  # Guardo a la base de datos.
            mensaje = f"El paciente {instancia_paciente_1.apellido} fue guardado con exito en nuestra base de datos. "
          
            # Guarde el nuevo item a la base de datos, ahora aviso por medio de la pagina y pongo el boton limpiar.
            return render(request,'app_gestion_bd/pacientes.html',{"formulario": formulario,"mensaje": mensaje,"boton_limpiar": True })

    
    else: # si metodo es get
        formulario = form_paciente()
        return render(request,'app_gestion_bd/pacientes.html',{"formulario": formulario})
    

def vista_usuarios_sistema(request):

    if request.method == 'POST':

        formulario = form_usuario(request.POST) #Creo un formulario medico que recibira un request.
        
        if formulario.is_valid():
            
            info_usuario = formulario.cleaned_data  #Agarro la informacion devuelta en un diccionario?
            
            instancia_usuario_1 = usuario(nombre= info_usuario['nombre'], # Genero la instancia.
                                    apellido= info_usuario['apellido'],
                                    dni = info_usuario['dni'])
            instancia_usuario_1.save()  # Guardo la instancia en la base de datos.
            
            # Genero un mensaje para mostrar en la pagina.
            mensaje = f"El usuario {instancia_usuario_1.apellido} fue guardado con exito en nuestra base de datos. "
          
            # Guarde el nuevo item a la base de datos, ahora aviso por medio de la pagina,pongo el boton limpiar y muestro la pagina.
            return render(request,'app_gestion_bd/usuarios.html',{"formulario": formulario,"mensaje": mensaje,"boton_limpiar": True })

    
    else: # si metodo es get
        formulario = form_usuario()
        return render(request,'app_gestion_bd/usuarios.html',{"formulario": formulario})

    
    

 

def vista_seccion_busquedas(request):

    
    if request.method == "GET": #Aca averiguo si el usuario quiere buscar medicos, pacientes o usuarios.
                                # De acuerdo a lo seleccionado muestro la pagina de busqeda pero con el form de busqueda correspondiente.
        
        respuesta_servidor = request.GET #Devuelve un diccionario {"nombre formulario":valor boton seleccionado }.
        
    
        if respuesta_servidor.get("sel_busqueda") == "busq_medicos": # Si devolvio el valor busq_medicos.
            formulario_busqueda = form_busqueda_medico()
            return render(request,'app_gestion_bd/busqueda.html',{'formulario_busqueda':formulario_busqueda, 'dibujar_formulario' : True})
        
        
        if respuesta_servidor.get("sel_busqueda") == "busq_pacientes": # Si devolvio el valor busq_pacientes.
            formulario_busqueda = form_busqueda_paciente()
            return render(request,'app_gestion_bd/busqueda.html',{'formulario_busqueda':formulario_busqueda, 'dibujar_formulario' : True})
    
        if respuesta_servidor.get("sel_busqueda") == "busq_usuarios": # Si devolvio el valor busq_usuarios.
            formulario_busqueda = form_busqueda_usuario()
            return render(request,'app_gestion_bd/busqueda.html',{'formulario_busqueda':formulario_busqueda, 'dibujar_formulario' : True})

   
    else: # Si el metodo es POST, o sea nos envio informacion.

        respuesta_servidor = request.POST 
        # De la respuesta del servidor saco doble informacion:
                            # 1- Que formulario se utilizo (Si medico, usuarios o pacientes.)
                            # 2- Lo que esta buscando el usuario del sitio.
        
        # Si "apellido_medico" esta en las claves del diccionario quiere decir que utilizo el formulario de busqueda de medicos.
        # Si "apellido_paciente" esta en las claves del diccionario quiere decir que utilizo el formulario de busqueda de paciente.
        # Si "apellido_usuario" esta en las claves del diccionario quiere decir que utilizo el formulario de busquedqa de usuario.



        if "apellido_medico" in respuesta_servidor.keys(): 
            elemento_buscado = respuesta_servidor.get("apellido_medico")
            objeto_en_bd = medico.objects.filter(apellido__iexact = elemento_buscado) # devuelve un diccionario de objetos que contienen el apellido.

                     
            # De acuerdo a existan uno o mas elementos como el buscado devolvere el mensaje.
            if len(objeto_en_bd) >=1: mensaje = "Existe uno o mas medicos con el apellido " + elemento_buscado
            else: mensaje = "NO EXISTEN uno o mas medicos con el apellido " + elemento_buscado
            
            return render(request,'app_gestion_bd/busqueda.html',{'resultado_busqueda':mensaje,'boton_limpiar': True})


            
        if "apellido_paciente" in respuesta_servidor.keys():
            elemento_buscado = respuesta_servidor.get("apellido_paciente")
            objeto_en_bd = paciente.objects.filter(apellido__iexact = elemento_buscado) # devuelve un diccionario de objetos que contienen el apellido.
            
            # De acuerdo a existan uno o mas elementos como el buscado devolvere el mensaje.
            if len(objeto_en_bd) >=1: mensaje = "Existe uno o mas pacientes con el apellido " + elemento_buscado 
            else: mensaje = "NO EXISTEN uno o mas pacientes con el apellido " + elemento_buscado
            
            return render(request,'app_gestion_bd/busqueda.html',{'resultado_busqueda':mensaje,'boton_limpiar': True})
            

        if "apellido_usuario" in respuesta_servidor.keys():
            elemento_buscado = respuesta_servidor.get("apellido_usuario")
            objeto_en_bd = usuario.objects.filter(apellido__iexact = elemento_buscado) # devuelve un diccionario de objetos que contienen el apellido.
            
            # De acuerdo a existan uno o mas elementos como el buscado devolvere el mensaje.
            if len(objeto_en_bd) >=1: mensaje = "Existe uno o mas usuarios con el apellido " + elemento_buscado 
            else: mensaje = "NO EXISTEN uno o mas usuarios con el apellido " + elemento_buscado

            #************************************************************************************
            
            #************************************************************************************
            
            return render(request,'app_gestion_bd/busqueda.html',{'resultado_busqueda':mensaje,'boton_limpiar': True})

    return render(request,'app_gestion_bd/busqueda.html')
    



def vista_guia(request):

    
    tabla_medicos = Template(tabla_codigos_html("especialidades"))
    tabla_obra_social = Template(tabla_codigos_html("obra_social"))

    return render(request,'app_gestion_bd/guia.html',{'tabla_medicos': tabla_medicos,'tabla_obra_social': tabla_obra_social} )



def vista_datos(request):

    
    if request.method == "GET": #Aca averiguo si el usuario quiere listar medicos, pacientes o usuarios.
                               
        
        respuesta_servidor = request.GET #Devuelve un diccionario {"nombre formulario":valor boton seleccionado }.
        
    
        if respuesta_servidor.get("sel_busqueda") == "busq_medicos": # Si devolvio el valor busq_medicos.
            
            lista_medicos = medico.objects.all()
            return render(request,'app_gestion_bd/datos.html',{'datos_solicitados': lista_medicos, 'mensaje': "Medicos ingresados en el sistema", 'dibujar_datos': True, 'boton_limpiar': True} )
            
                 
        if respuesta_servidor.get("sel_busqueda") == "busq_pacientes": # Si devolvio el valor busq_pacientes.
           lista_medicos = paciente.objects.all()
           return render(request,'app_gestion_bd/datos.html',{'datos_solicitados': lista_medicos, 'mensaje': "Pacientes ingresados en el sistema.", 'dibujar_datos': True, 'boton_limpiar': True} )
    
        if respuesta_servidor.get("sel_busqueda") == "busq_usuarios": # Si devolvio el valor busq_usuarios.
           lista_medicos = usuario.objects.all()
           return render(request,'app_gestion_bd/datos.html',{'datos_solicitados': lista_medicos, 'mensaje': "Personas autorizadas a usar este sistema.", 'dibujar_datos': True, 'boton_limpiar': True} )

    
    return render(request,'app_gestion_bd/datos.html' )
   
   