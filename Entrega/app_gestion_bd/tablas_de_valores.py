#En este modulo vamos a poner todos los datos de codigos que usaremos en los menues de seleccion para poder traducirlos y modificarlos.
import pandas as pd

lista_especialidades = [(1, "Otorrinolaringologia"), # Lista de tuplas.
                        (2, "Nutricion"),
                        (3, "Psicologia"),
                        (4, "Fonoaudiologia"),
                        (5, "Odontologia"),
                        (6, "Clinica"),
                        (7, "Ginecologia"),
                        (8, "Pediatria")] 

lista_obras_sociales = [(1, "OSDE"), # Lista de tuplas.
                        (2, "GALENO"),
                        (3, "IOMA"),
                        (4, "CEDIMEC"),
                        (5, "OSFE"),
                        (6, "OSECACO"),
                        (7, "MEDIFES"),
                        (8, "Otra")] 


# Devuelve el nombre del valor de item pasado por parametro.
def get_nombre_especialidad(valor):

    encontrado = ""
    
    for elemento in lista_especialidades:

        if elemento[0] == valor: 
            encontrado = elemento[1]
            break

    return encontrado

def get_nombre_obra_social(valor):

    encontrado = ""
    
    for elemento in lista_obras_sociales:

        if elemento[0] == valor: 
            encontrado = elemento[1]
            break

    return encontrado


def tabla_codigos_html(criterio): # Devuelve una tabla en html para mostrar al usuario del sistema y tener referencias.

    mi_tabla = ""
    if criterio == "obra_social": 
        mi_tabla = lista_obras_sociales
        nombre_cols = ("Codigo","Nombre")
    
    elif criterio == "especialidades": 
        mi_tabla = lista_especialidades
        nombre_cols =("Codigo","Especialidad")

    df = pd.DataFrame(mi_tabla,columns=nombre_cols)
    
    
    html = pd.DataFrame.to_html(df,index=False)
    return html


