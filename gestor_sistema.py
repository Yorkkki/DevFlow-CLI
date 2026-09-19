from utils import *
from menu import *
def menu_sistema(cuentas_registradas, proyectos_registrados, sub_op):
    if sub_op == 18:
        print("Guardando datos...")
        usuarios_serializados = []
        for u in cuentas_registradas:
            usuarios_serializados.append({
                "id": u.id,
                "nombre": u.nombre,
                "correo": u.correo,
                "password_hash": u.obtener_password_hash(),
                "rol": u.rol
            })
        proyectos_serializados = []
        for p in proyectos_registrados:
            tareas_del_proyecto = []
            for t in p.tareas:
                tareas_del_proyecto.append({
                    "id": t.id,
                    "titulo": t.titulo,
                    "descripcion": t.descripcion,
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
                    tarea = Tarea(
                        id=t["id"],
                        titulo=t["titulo"],
                        descripcion=t.get("descripcion"),
                        prioridad=t.get("prioridad"),
                        estado=t.get("estado"),
                        fecha_limite=t.get("fecha_limite"),
                        horas=t.get("horas"),
                        comentarios=t.get("comentarios", [])
                    )
                    
                    proyecto.tareas.append(tarea)
                proyectos_registrados.append(proyecto)
            print("¡Datos cargados con éxito desde 'datos_sistema.json'!")
        except FileNotFoundError:
            print("No se encontró el archivo 'datos_sistema.json'. Asegúrese de guardarlo primero.")
        except Exception as e:
            print(f"Ocurrió un error al cargar los datos: {e}")
    elif sub_op == 20:
        print("Cerrando sesión...")
    elif sub_op == 21:
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Intente nuevamente.") 