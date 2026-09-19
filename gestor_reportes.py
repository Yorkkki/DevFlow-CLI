from utils import *
from menu import *
def menu_reportes(proyectos_registrados, sub_op):
    if sub_op == 14:
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