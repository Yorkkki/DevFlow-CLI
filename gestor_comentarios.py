from utils import *
def menu_comentarios(proyectos_registrados, sub_op):
    if sub_op == 12: 
        if not proyectos_registrados:
            print("No hay proyectos registrados.")
        else:
            id_proyecto_buscar = pedir_numero_seguro("Ingrese el ID del proyecto donde está la tarea que desea agregar el comentario: ")
            proyecto_encontrado = None
            for proyecto in proyectos_registrados:
                if proyecto.id == id_proyecto_buscar:
                    proyecto_encontrado = proyecto
                    break
            if proyecto_encontrado:
                if not proyecto_encontrado.tareas:
                    print(f"El proyecto {proyecto_encontrado.nombre} no tiene tareas.")
                else: 
                    nombre_tarea_buscar = input("Escriba el nombre de la tarea que desea agregar el comentario: ").strip().lower()
                    nombre_a_comentar = None
                    for tarea in proyecto_encontrado.tareas:
                        if tarea.titulo.strip().lower() == nombre_tarea_buscar:
                            tarea_a_comentar = tarea
                            break
                    if tarea_a_comentar is not None:
                        agregar_comentario = input("Agregue el comentario de la tarea: ")
                        tarea_a_comentar.agregar_comentario(agregar_comentario)
                        print("Se agrego el comentario!")
                    else:
                        print("Error: No se encontró ninguna tarea con ese nombre en este proyecto")  
            else:
                print("Error: No se encontró ningún proyecto con ese ID.")
    
    elif sub_op == 13:
        if not proyectos_registrados:
            print("No hay proyectos registrados.")
        else:
            id_proyecto_buscar = pedir_numero_seguro("Ingrese el ID del proyecto donde está la tarea que desea ver el comentario: ")
            proyecto_encontrado = None
            for proyecto in proyectos_registrados:
                if proyecto.id == id_proyecto_buscar:
                    proyecto_encontrado = proyecto
                    break
            if proyecto_encontrado:
                if not proyecto_encontrado.tareas:
                    print(f"El proyecto {proyecto_encontrado.nombre} no tiene tareas.")
                else: 
                    nombre_tarea_buscar = input("Escriba el titulo de la tarea que desea ver los comentarios: ").strip().lower()
                    tarea_ver_comentario = None
                    for tarea in proyecto_encontrado.tareas:
                        if tarea.titulo.strip().lower() == nombre_tarea_buscar:
                            tarea_ver_comentario = tarea
                            break     
                    if tarea_ver_comentario is not None:
                        if not tarea_ver_comentario.comentarios:
                            print(f"La tarea '{tarea_ver_comentario.titulo}' no tiene comentarios aún.")
                        else:
                            print(f"\n=== Comentarios de la tarea: {tarea_ver_comentario.titulo} ===")
                            for comentario in tarea_ver_comentario.comentarios:
                                print(f"- {comentario}")
                    else:
                        print("Error: No se encontró ninguna tarea con ese nombre en este proyecto")  
            else:
                print("Error: No se encontró ningún proyecto con ese ID.")
    