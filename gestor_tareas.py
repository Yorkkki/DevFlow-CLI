from tarea import Tarea
from utils import *
def menu_tareas(proyectos_registrados, sub_op):
    if sub_op == 6:
        if not proyectos_registrados:
            print("No hay proyectos registrados.")
        else:
            nombre_proyecto = input("Ingrese el nombre del proyecto al que desea agregar la tarea: ")
            proyecto_encontrado = None
            for proyecto in proyectos_registrados:
                #sirve para ignorar mayúsculas y minúsculas al buscar el proyecto
                if proyecto.nombre.strip().lower() == nombre_proyecto.strip().lower():
                    proyecto_encontrado = proyecto
                    break
            if proyecto_encontrado:
                nombre_tarea = input("Ingrese el nombre de la tarea: ")
                descripcion_tarea = input("Ingrese la descripción de la tarea: ")
                responsable_tarea = input("Ingrese el nombre del responsable de la tarea: ")
                estado_tarea = input("Ingrese el estado de la tarea (pendiente/completada): ")
                id_tarea = len(proyecto_encontrado.tareas) + 1
                nueva_tarea = Tarea(id_tarea, nombre_tarea, descripcion_tarea, None, estado_tarea, None, None, [])
                proyecto_encontrado.tareas.append(nueva_tarea)
                print(f"Tarea '{nombre_tarea}' agregada al proyecto '{proyecto_encontrado.nombre}' con éxito.")
    
    elif sub_op == 7:
        if not proyectos_registrados:
            print("No hay proyectos registrados.")
        else:
            nombre_proyecto = input("Ingrese el nombre del proyecto cuyas tareas desea ver: ")
            proyecto_encontrado = None
            for proyecto in proyectos_registrados:
                if proyecto.nombre.strip().lower() == nombre_proyecto.strip().lower():
                    proyecto_encontrado = proyecto
                    break
            if proyecto_encontrado:
                if not proyecto_encontrado.tareas:
                    print(f"No hay tareas registradas para el proyecto {proyecto_encontrado.nombre}.")
                else:
                    print(f"=== Tareas del Proyecto: {proyecto_encontrado.nombre} ===")
                    for tarea in proyecto_encontrado.tareas:
                        print(f"- {tarea.titulo}: {tarea.descripcion},Estado: {tarea.estado})")
    
    elif sub_op == 8:
        if not proyectos_registrados:
            print("No hay proyectos registrados.")
        else:             
            id_proyecto_buscar = pedir_numero_seguro("Ingrese el ID del proyecto: ")
            proyecto_encontrado = None
            for proyectos in proyectos_registrados:
                if proyectos.id == id_proyecto_buscar:
                    proyecto_encontrado = proyectos
                    break
            if proyecto_encontrado:
                if not proyecto_encontrado.tareas:
                    print (f"No hay tareas registradas para el proyecto {proyecto_encontrado.nombre}.")
                else: 
                    print(f"=== Tareas del Proyecto: {proyecto_encontrado.nombre} ===")
                    for tarea in proyecto_encontrado.tareas:
                        print(f"- {tarea.titulo}: {tarea.descripcion},Estado: {tarea.estado})")
            else:
                print("Error: No se encontró ningún proyecto con ese ID.")
    
    elif sub_op == 9:
        if not proyectos_registrados:
            print("No hay proyectos registrados.")
        else:
            id_proyecto_buscar = pedir_numero_seguro("Ingrese el ID del proyecto donde está la tarea: ")
            proyecto_encontrado = None
        
        for proyecto in proyectos_registrados:
            if proyecto.id == id_proyecto_buscar:
                proyecto_encontrado = proyecto
                break
        if proyecto_encontrado:
            if not proyecto_encontrado.tareas:
                print(f"El proyecto {proyecto_encontrado.nombre} no tiene tareas.")
            else:
                nombre_tarea_buscar = input("Escriba el nombre de la tarea a cambiar estado: ").strip().lower()
                tarea_encontrada = None
                
                for tarea in proyecto_encontrado.tareas:
                    if tarea.nombre.strip().lower() == nombre_tarea_buscar:
                        tarea_encontrada = tarea
                        break
                if tarea_encontrada:
                    print(f"Estado actual de la tarea: {tarea_encontrada.estado}")
                    nuevo_estado = input("Escriba el nuevo estado de la tarea: ")
                    tarea_encontrada.estado = nuevo_estado
                    print(f"¡Estado de la tarea '{tarea_encontrada.nombre}' actualizado con éxito!")
                else:
                    print("Error: No se encontró ninguna tarea con ese nombre en este proyecto.")
        else: 
            print("Error: No se encontró ningún proyecto con ese ID.")
    
    elif sub_op == 10:
        if not proyectos_registrados:
            print("No hay proyectos registrados.")
        else:
            id_proyecto_buscar = pedir_numero_seguro("Ingrese el ID del proyecto donde está la tarea a modificar: ")
            proyecto_encontrado = None
        
        for proyecto in proyectos_registrados:
            if proyecto.id == id_proyecto_buscar:
                proyecto_encontrado = proyecto
                break
        if proyecto_encontrado:
            if not proyecto_encontrado.tareas:
                print(f"El proyecto {proyecto_encontrado.nombre} no tiene tareas.")
            else:
                nombre_tarea_buscar = input("Escriba el nombre de la tarea que desea modificar: ").strip().lower()
                tarea_encontrada = None
            for tarea in proyecto_encontrado.tareas:
                    if tarea.titulo.strip().lower() == nombre_tarea_buscar:
                        tarea_encontrada = tarea
                        break
            if tarea_encontrada:
                print("\n--- Datos actuales de la tarea ---")
                tarea_encontrada.mostrar_tarea()
                print(f"La tarea es: {tarea_encontrada.mostrartarea()}")
                nuevo_titulo = input("Escriba el nuevo titulo de la tarea: ")
                tarea_encontrada.titulo = nuevo_titulo
                nueva_descripcion = input("Escriba la nueva descripcion de la tarea: ")
                tarea_encontrada.descripcion = nueva_descripcion
                print(f"¡Tarea '{tarea_encontrada.nombre}' actualizada con éxito!")
            else:
                print("Error: No se encontró ninguna tarea con ese nombre en este proyecto.")
    
    elif sub_op == 11:
        if not proyectos_registrados:
            print("No hay proyectos registrados.")
        else:
            id_proyecto_buscar = pedir_numero_seguro("Ingrese el ID del proyecto donde está la tarea a eliminar: ")
            proyecto_encontrado = None
            for proyecto in proyectos_registrados:
                if proyecto.id == id_proyecto_buscar:
                    proyecto_encontrado = proyecto
                    break
            if proyecto_encontrado:
                if not proyecto_encontrado.tareas:
                    print(f"El proyecto {proyecto_encontrado.nombre} no tiene tareas.")
                else:
                    nombre_tarea_buscar = input("Escriba el nombre de la tarea que desea eliminar: ").strip().lower()
                    tarea_a_eliminar = None
                    for tarea in proyecto_encontrado.tareas:
                        if tarea.nombre.strip().lower() == nombre_tarea_buscar:
                            tarea_a_eliminar = tarea
                            break
                    if tarea_a_eliminar is not None:
                        proyecto_encontrado.tareas.remove(tarea_a_eliminar)
                        print(f"Tarea '{tarea_a_eliminar.nombre}' eliminada con éxito del proyecto '{proyecto_encontrado.nombre}'.")
                    else:
                        print("Error: No se encontró ninguna tarea con ese nombre en este proyecto")