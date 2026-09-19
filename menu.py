from matplotlib.pylab import rint
from usuario import Usuario
from gestor_proyectos import menu_proyectos
from gestor_tareas import menu_tareas
from gestor_comentarios import menu_comentarios
from gestor_reportes import menu_reportes
from gestor_sistema import menu_sistema
from utils import *
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

        try:
            op = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
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
                    
                    try:
                        sub_op = int(input("Seleccione una opción: "))
                    except ValueError:
                        print("Por favor, ingresa un número válido.")
                        continue
                    
                    # Llamar a la función menu_proyectos para manejar las opciones del menú opciones del 1-5
                    if sub_op in range(1, 6):
                        menu_proyectos(proyectos_registrados, sub_op)
                    
                    # Llamar a la función menu_tareas para manejar las opciones del menú opciones del 6-11    
                    elif sub_op in range(6, 12):
                        menu_tareas(proyectos_registrados, sub_op)
                    
                    # Llamar a la función menu_comentarios para manejar las opciones del menú opciones del 12-13
                    elif sub_op in range(12, 14):
                        menu_comentarios(proyectos_registrados, sub_op)
                    
                    elif sub_op in range(14, 18):
                        menu_reportes(proyectos_registrados, cuentas_registradas, sub_op)
                        
                    elif sub_op in range(18, 22):
                        menu_sistema(cuentas_registradas, proyectos_registrados, sub_op)
                        if sub_op == 20:
                            break  # Salir del bucle para cerrar sesión
                        elif sub_op == 21:
                            exit()  # Salir del programa
            else:
                print("Correo o contraseña incorrectos.")
        
        elif op == 2:
            correo_existe = False
            print("=== Registro de usuario ===")
            nombre = input("Ingrese su nombre: ")
            correo = input("Ingrese su correo: ")
            for usuario in cuentas_registradas:
                if usuario.correo == correo:
                    correo_existe = True
                    break
            if correo_existe:
                print("El correo ya está registrado.")
            else:
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