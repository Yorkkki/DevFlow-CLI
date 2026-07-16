class Tarea:
    def __init__(self, id, titulo, prioridad, estado, fecha_limite, horas, comentarios):
        self.id = id
        self.titulo = titulo
        self.prioridad = prioridad
        self.estado = estado
        self.fecha_limite = fecha_limite
        self.horas = horas
        self.comentarios = comentarios

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    def agregar_comentario(self, comentario):
        self.comentarios.append(comentario)
    
    def editar_tarea(self, nuevo_titulo=None, nueva_prioridad=None, nueva_fecha_limite=None, nuevas_horas=None):
        if nuevo_titulo:
            self.titulo = nuevo_titulo
        if nueva_prioridad:
            self.prioridad = nueva_prioridad
        if nueva_fecha_limite:
            self.fecha_limite = nueva_fecha_limite
        if nuevas_horas:
            self.horas = nuevas_horas
    
    def mostrar_tarea(self):
        print(f"ID: {self.id}")
        print(f"Título: {self.titulo}")
        print(f"Prioridad: {self.prioridad}")
        print(f"Estado: {self.estado}")
        print(f"Fecha límite: {self.fecha_limite}")
        print(f"Horas estimadas: {self.horas}")
        print("Comentarios:")
        for comentario in self.comentarios:
            print(f"- {comentario}")