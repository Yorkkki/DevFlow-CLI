from proyecto import Proyecto
def menu_proyectos(proyectos_registrados, sub_op):
    
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
            proyecto_encontrado = None
            for proyecto in proyectos_registrados:
                if proyecto.nombre.strip().lower() == nombre_buscar_p.strip().lower():
                    proyecto_encontrado = proyecto
                    break
            if proyecto_encontrado is not None:
                    print(f"Proyecto encontrado: {proyecto_encontrado.nombre}")
                    proyecto_encontrado.mostrar_proyecto()
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
        proyecto_a_eliminar = None
        
        for proyecto in proyectos_registrados:
            if proyecto.nombre.strip().lower() == nombre_buscar_p.strip().lower():
                proyecto_a_eliminar = proyecto
                break
            
        if proyecto_a_eliminar is not None:
            proyectos_registrados.remove(proyecto_a_eliminar)
            print(f"Proyecto '{proyecto_a_eliminar.nombre}' eliminado con éxito.")
        if not encontrado:
            print("Error: El proyecto no se encuentra registrado.")