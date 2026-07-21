from usuario import Usuario
from proyecto import Proyecto
import hashlib

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
                    print("14. Agregar comentario")
                    print("15. Ver comentarios")
                    print("")
                    print("===== REPORTES =====")
                    print("16. Ver tareas pendientes")
                    print("17. Ver tareas completadas")
                    print("18. Ver proyectos activos")
                    print("19. Estadisticas")
                    print("")
                    print("===== SISTEMA =====")
                    print("20. Guardar datos")
                    print("21. Cargar datos")
                    print("22. Cerrar sesión")
                    print("23. Salir")
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
                    
                    elif sub_op == 22:
                        print("Cerrando sesión...")
                        break
                    elif sub_op == 23:
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