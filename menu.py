from matplotlib.pylab import rint

from usuario import Usuario
from proyecto import Proyecto
import hashlib
import json

cuentas_registradas = []
proyectos_registrados = []
def mostrar_menu():
    while True:
        print("=== Menu ===")
        print("1. Iniciar sesión")
        print("2. Registrar usuario")
        print("")

        op = int(input("Seleccione una opción: "))
        
        if op == 1:
            input_correo = input("Ingrese su correo: ")
            input_password = input("Ingrese su contraseña: ")
            usuario_encontrado = None
            for u in cuentas_registradas:
                if u.correo == input_correo and u.verificar_password(input_password):
                    usuario_encontrado = u
                    break
            if usuario_encontrado:
                print(f"Bienvenido, {usuario_encontrado.nombre}!")
                usuario_encontrado.mostrar_datos()
                while True:
                    print("===== PROYECTOS =====")
                    print("1. Crear proyecto")
                    print("2. Ver proyectos")
                    print("3. Buscar proyecto")
                    print("4. Editar proyecto")
                    print("5. Eliminar proyecto")
                    print("")
                    print("===== TAREAS =====")
                    print("6. Crear tarea")
                    print("7. Ver tareas")
                    print("8. Buscar tarea")
                    print("9. Cambiar estado de tarea")
                    print("10. Editar tarea")
                    print("11. Eliminar tarea")
                    print("")
                    print("===== COMENTARIOS =====")
                    print("12. Agregar comentario")
                    print("13. Ver comentarios")
                    print("")
                    print("===== REPORTES =====")
                    print("14. Ver tareas pendientes")
                    print("15. Ver tareas completadas")
                    print("16. Ver proyectos activos")
                    print("17. Estadisticas")
                    print("")
                    print("===== SISTEMA =====")
                    print("18. Guardar datos")
                    print("19. Cargar datos")
                    print("20. Cerrar sesión")
                    print("21. Salir")
                    print("============")
                    
                    sub_op = int(input("Seleccione una opción: "))
                    
                    if sub_op == 1:
                        nombre_proyecto = input(f"Escriba el nombre de su proyecto nuevo: ")
                        descripcion_p = input(f"Escriba la descripción de su proyecto nuevo: ")
                        responsable_p = input(f"Escriba el nombre del responsable de su proyecto nuevo: ")
                        id_proyecto = len(proyectos_registrados) + 1
                        nuevo_proyecto = Proyecto(
                            id = id_proyecto,
                            nombre=nombre_proyecto,
                            descripcion= descripcion_p,
                            fecha_creacion= None,
                            estado=None,
                            responsable=responsable_p,
                            tareas=[]
                        )
                        proyectos_registrados.append(nuevo_proyecto)
                        print(f"¡Proyecto '{nuevo_proyecto.nombre}' creado con éxito!")
                        
                    elif sub_op == 2:
                        if not proyectos_registrados:
                            print("No hay proyectos registrados.")
                        else:
                            print("=== Proyectos Registrados ===")
                            for proyecto in proyectos_registrados:
                                proyecto.mostrar_proyecto()
                    
                    elif sub_op == 3:
                        if not proyectos_registrados:
                            print("No hay proyectos registrados.")
                        else:
                            nombre_buscar_p = input("Escriba el nombre del proyecto que desea buscar: ")
                            for proyecto in proyectos_registrados:
                                if proyecto.nombre == nombre_buscar_p:
                                    print("Proyecto encontrado!")
                                    proyecto.mostrar_proyecto()
                                else:
                                    print(f"No hay proyectos registrados con el nombre de: {nombre_buscar_p}")
                    
                    elif sub_op == 4:
                        nombre_buscar_p = input("Escriba el nombre del proyecto que desea editar: ")
                        encontrado = False
                        for i in range (len(proyectos_registrados)):
                            if proyectos_registrados[i].nombre == nombre_buscar_p.strip().lower():
                                encontrado = True
                                proyecto = proyectos_registrados[i]
                                
                                print(f"\n--- Editando Proyecto: {proyecto.nombre} ---")
                                print("1. Editar Nombre")
                                print("2. Editar Descripción")
                                print("3. Editar responsable")
                                sub_op = input("Seleccione una opción (1-3): ")
                                
                                if sub_op == "1":
                                    nuevo_nombre = input("Escriba el nuevo nombre: ")
                                    proyecto.nombre = nuevo_nombre
                                    print("¡Nombre actualizado con éxito!")
                                elif sub_op == "2":
                                    nueva_desc = input("Escriba la nueva descripción: ")
                                    proyecto.descripcion = nueva_desc
                                    print("¡Descripción actualizada con éxito!")
                                elif sub_op == "3":
                                    nuevo_responsable = input("Escriba el nuevo responsable: ")
                                    proyecto.responsable = nuevo_responsable
                                    print("¡Responsable actualizado con éxito!")
                                else:
                                    print("Opción inválida. No se realizaron cambios.")
                                break
                                
                        if not encontrado: 
                            print("Error: El proyecto no se encuentra registrado.")
                    
                    elif sub_op == 5:
                        nombre_buscar_p = input("Escriba el nombre del proyecto que desea eliminar: ")
                        encontrado = False
                        for proyecto in proyectos_registrados:
                            if proyecto.nombre.strip().lower() == nombre_buscar_p.strip().lower():
                                proyecto_a_eliminar = proyecto
                                break
                        if proyecto_a_eliminar is not None:
                            proyectos_registrados.remove(proyecto_a_eliminar)
                            print(f"Proyecto '{proyecto_a_eliminar.nombre}' eliminado con éxito.")
                        if not encontrado:
                            print("Error: El proyecto no se encuentra registrado.")
                    
                    elif sub_op == 6:
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
                                nueva_tarea = {
                                    "id": id_tarea,
                                    "nombre": nombre_tarea,
                                    "descripcion": descripcion_tarea,
                                    "responsable": responsable_tarea,
                                    "estado": estado_tarea,
                                    "comentarios": []
                                }
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
                                        print(f"- {tarea['nombre']}: {tarea['descripcion']} (Responsable: {tarea['responsable']}, Estado: {tarea['estado']})")
                    
                    elif sub_op == 8:
                        if not proyectos_registrados:
                            print("No hay proyectos registrados.")
                        else: 
                            id_proyecto_buscar = int(input("Ingrese el ID del proyecto: "))
                            proyecto_encontrado = None
                            for proyectos in proyectos_registrados:
                                if proyecto.id == id_proyecto_buscar:
                                    proyecto_encontrado = proyectos
                                    break
                            if proyecto_encontrado:
                                if not proyecto_encontrado.tareas:
                                    print (f"No hay tareas registradas para el proyecto {proyecto_encontrado.nombre}.")
                                else: 
                                    print(f"=== Tareas del Proyecto: {proyecto_encontrado.nombre} ===")
                                    for tarea in proyecto_encontrado.tareas:
                                        print(f"- {tarea.nombre}: {tarea.descripcion} (Responsable: {tarea.responsable}, Estado: {tarea.estado})")
                            else:
                                print("Error: No se encontró ningún proyecto con ese ID.")
                    
                    elif sub_op == 9:
                        if not proyectos_registrados:
                            print("No hay proyectos registrados.")
                        else:
                            id_proyecto_buscar = int(input("Ingrese el ID del proyecto donde está la tarea: "))
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
                            id_proyecto_buscar = int(input("Ingrese el ID del proyecto donde está la tarea a modificar: "))
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
                            id_proyecto_buscar = int(input("Ingrese el ID del proyecto donde está la tarea a eliminar: "))
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
                    
                    elif sub_op == 12: 
                        if not proyectos_registrados:
                            print("No hay proyectos registrados.")
                        else:
                            id_proyecto_buscar = int(input("Ingrese el ID del proyecto donde está la tarea que desea agregar el comentario: "))
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
                            id_proyecto_buscar = int(input("Ingrese el ID del proyecto donde está la tarea que desea ver el comentario: "))
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
                    
                    elif sub_op == 14:
                        if not proyectos_registrados:
                            print("No hay proyectos registrados.")
                        else:
                            print("=== Tareas Pendientes ===")
                            for proyecto in proyectos_registrados:
                                for tarea in proyecto.tareas:
                                    if tarea.estado.strip().lower() == "pendiente":
                                        print(f"- Proyecto: {proyecto.nombre}, Tarea: {tarea.titulo}, Responsable: {tarea.responsable}")

                    elif sub_op == 15:
                        if not proyectos_registrados:
                            print("No hay proyectos registrados.")
                        else:
                            print("=== Tareas Completadas ===")
                            for proyecto in proyectos_registrados:
                                for tarea in proyecto.tareas:
                                    if tarea.estado.strip().lower() == "completada":
                                        print(f"- Proyecto: {proyecto.nombre}, Tarea: {tarea.titulo}, Responsable: {tarea.responsable}")

                    elif sub_op == 16:
                        if not proyectos_registrados:
                            print("No hay proyectos registrados.")
                        else:
                            print("=== Proyectos Activos ===")
                            for proyecto in proyectos_registrados:
                                if proyecto.estado.strip().lower() == "activo":
                                    print(f"- Proyecto: {proyecto.nombre}, Responsable: {proyecto.responsable}")

                    elif sub_op == 17:
                        if not proyectos_registrados:
                            print("No hay proyectos registrados.")
                        else:
                            total_usuarios = len(cuentas_registradas)
                            total_proyectos = len(proyectos_registrados)
                            total_tareas = sum(len(proyecto.tareas) for proyecto in proyectos_registrados)
                            total_tareas_pendientes = sum(1 for proyecto in proyectos_registrados for tarea in proyecto.tareas if tarea.estado.strip().lower() == "pendiente")
                            total_tareas_completadas = sum(1 for proyecto in proyectos_registrados for tarea in proyecto.tareas if tarea.estado.strip().lower() == "completada")
                            print("=== Estadísticas del Sistema ===")
                            print(f"Total de usuarios registrados: {total_usuarios}")
                            print(f"Total de proyectos registrados: {total_proyectos}")
                            print(f"Total de tareas registradas: {total_tareas}")
                            print(f"Total de tareas pendientes: {total_tareas_pendientes}")
                            print(f"Total de tareas completadas: {total_tareas_completadas}")
                    
                    elif sub_op == 18:
                        print("Guardando datos...")
                        usuarios_serializados = []
                        for u in cuentas_registradas:
                            usuarios_serializados.append({
                                "id": u.id,
                                "nombre": u.nombre,
                                "correo": u.correo,
                                "password_hash": u.password_hash,
                                "rol": u.rol
                            })
                        proyectos_serializados = []
                        for p in proyectos_registrados:
                            tareas_del_proyecto = []
                            for t in p.tareas:
                                tareas_del_proyecto.append({
                                    "id": t.id,
                                    "titulo": t.titulo,
                                    "prioridad": t.prioridad,
                                    "estado": t.estado,
                                    "fecha_limite": t.fecha_limite,
                                    "horas": t.horas,
                                    "comentarios": t.comentarios 
                                })
                            proyectos_serializados.append({
                                "id": p.id,
                                "nombre": p.nombre,
                                "descripcion": p.descripcion,
                                "fecha_inicio": p.fecha_inicio,
                                "fecha_fin": p.fecha_fin,
                                "estado": p.estado,
                                "responsable": p.responsable,
                                "tareas": tareas_del_proyecto
                            })
                        proyectos_serializados.append({
                            "id": p.id,
                            "nombre": p.nombre,
                            "descripcion": p.descripcion,
                            "fecha_creacion": p.fecha_creacion,
                            "estado": p.estado,
                            "responsable": p.responsable,
                            "tareas": tareas_del_proyecto
                        })
                        datos_totales = {
                            "usuarios": usuarios_serializados,
                            "proyectos": proyectos_serializados
                        }
                        try:
                            with open("datos_sistema.json", "w", encoding="utf-8") as archivo:
                                # indent=4 sirve para que el archivo se vea ordenado y bonito si lo abres
                                json.dump(datos_totales, archivo, indent=4, ensure_ascii=False)
                            print("¡Datos guardados con éxito en 'datos_sistema.json'!")
                        except Exception as e:
                            print(f"Ocurrió un error al guardar los datos: {e}")
                    
                    elif sub_op == 19:
                        print("Cargando datos...")
                        try:
                            with open("datos_sistema.json", "r", encoding="utf-8") as archivo:
                                datos_cargados = json.load(archivo)
                            cuentas_registradas.clear()
                            for u in datos_cargados.get("usuarios", []):
                                usuario = Usuario(
                                    id=u["id"],
                                    nombre=u["nombre"],
                                    correo=u["correo"],
                                    password_hash=u["password_hash"],
                                    rol=u["rol"]
                                )
                                cuentas_registradas.append(usuario)
                            proyectos_registrados.clear()
                            for p in datos_cargados.get("proyectos", []):
                                proyecto = Proyecto(
                                    id=p["id"],
                                    nombre=p["nombre"],
                                    descripcion=p["descripcion"],
                                    fecha_creacion=p.get("fecha_creacion"),
                                    estado=p.get("estado"),
                                    responsable=p.get("responsable"),
                                    tareas=[]
                                )
                                for t in p.get("tareas", []):
                                    tarea = {
                                        "id": t["id"],
                                        "titulo": t["titulo"],
                                        "prioridad": t.get("prioridad"),
                                        "estado": t.get("estado"),
                                        "fecha_limite": t.get("fecha_limite"),
                                        "horas": t.get("horas"),
                                        "comentarios": t.get("comentarios", [])
                                    }
                                    proyecto.tareas.append(tarea)
                                proyectos_registrados.append(proyecto)
                            print("¡Datos cargados con éxito desde 'datos_sistema.json'!")
                        except FileNotFoundError:
                            print("No se encontró el archivo 'datos_sistema.json'. Asegúrese de guardarlo primero.")
                        except Exception as e:
                            print(f"Ocurrió un error al cargar los datos: {e}")
                    elif sub_op == 20:
                        print("Cerrando sesión...")
                        break
                    elif sub_op == 21:
                        print("Saliendo del programa...")
                        exit()
                    else:
                        print("Opción inválida. Intente nuevamente.") 
                    
            else:
                print("Correo o contraseña incorrectos.")
        
        elif op == 2:
            print("=== Registro de usuario ===")
            nombre = input("Ingrese su nombre: ")
            correo = input("Ingrese su correo: ")
            password = input("Ingrese su contraseña: ")
            # El ID se calcula automáticamente según cuántos usuariosya existen
            id_automatico = len(cuentas_registradas) + 1 # Genera un ID único basado en la cantidad de usuarios
            password_encriptada = hashlib.sha256(password.encode()).hexdigest() #sirve para encriptar la contraseña en texto plano
            nuevo_usuario = Usuario(
                id = id_automatico,
                nombre = nombre,
                correo = correo,
                password_hash = password_encriptada,
                rol = "Usuario"
                )
            cuentas_registradas.append(nuevo_usuario)
            print(f"¡Usuario registrado con éxito! Tu ID asignado es: {nuevo_usuario.id}")