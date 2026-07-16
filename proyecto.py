class Proyecto:
    def __init__(self, nombre, descripcion, fecha_creacion, estado, responsable, tareas):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_creacion = fecha_creacion
        self.estado = estado
        self.responsable = responsable
        self.tareas = tareas
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea agregada con éxito al proyecto '{self.nombre}'.")
        

    def eliminar_tarea(self, tarea):
        self.tareas.remove(tarea)
    
    def buscar_tarea(self, nombre_tarea):
        for tarea in self.tareas:
            if tarea.nombre == nombre_tarea:
                return tarea
        return None

    def mostrar_proyecto(self):
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Fecha de creación: {self.fecha_creacion}")
        print(f"Estado: {self.estado}")
        print(f"Responsable: {self.responsable}")
        print("Tareas:")
        for tarea in self.tareas:
            tarea.mostrar_tarea()