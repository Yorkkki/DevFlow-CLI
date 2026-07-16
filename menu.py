from random import random
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
            fecha_creacion_p = input(f"Escriba la fecha de creación de su proyecto nuevo (formato: dd/mm/aaaa): ")
            estado_p = input(f"Escriba el estado de su proyecto nuevo (Activo/Inactivo): ")
            responsable_p = input(f"Escriba el nombre del responsable de su proyecto nuevo: ")
            id_proyecto = len(proyectos_registrados) + 1
            nuevo_proyecto = Proyecto(
                nombre=nombre_proyecto,
                descripcion= descripcion_p,
                fecha_creacion= fecha_creacion_p,
                estado=estado_p,
                responsable=responsable_p,
                tareas=[]
            )
            proyectos_registrados.append(nuevo_proyecto)
            print(f"¡Proyecto '{nuevo_proyecto.nombre}' creado con éxito!")
        
        elif op == 22:
            print("Cerrando sesión...")
            break
        elif op == 23:
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción inválida. Intente nuevamente.")    