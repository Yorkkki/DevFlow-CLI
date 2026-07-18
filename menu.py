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
        print("===== PROYECTOS =====")
        print("3. Crear proyecto")
        print("4. Ver proyectos")
        print("5. Buscar proyecto")
        print("6. Editar proyecto")
        print("7. Eliminar proyecto")
        print("")
        print("===== TAREAS =====")
        print("8. Crear tarea")
        print("9. Ver tareas")
        print("10. Buscar tarea")
        print("11. Cambiar estado de tarea")
        print("12. Editar tarea")
        print("13. Eliminar tarea")
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

        op = int(input("Seleccione una opción (1-23): "))
        
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
            pass
        
        elif op == 3:
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
            
        elif op == 4:
            if not proyectos_registrados:
                print("No hay proyectos registrados.")
            else:
                print("=== Proyectos Registrados ===")
                for proyecto in proyectos_registrados:
                    proyecto.mostrar_proyecto()
        
        elif op == 5:
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
        
        elif op == 6:
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
                
        elif op == 7:
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

        elif op == 22:
            print("Cerrando sesión...")
            break
        elif op == 23:
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción inválida. Intente nuevamente.")    