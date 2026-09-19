import hashlib
class Usuario:
    def __init__(self, id, nombre, correo, password_hash, rol= "Usuario"):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        #sirve para almacenar el hash de la contraseña en lugar de la contraseña en texto plano
        self.__password_hash = password_hash
        self.rol = rol

    #sirve para verificar si la contraseña ingresada coincide con el hash almacenado
    def __generar_hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    #sirve para generar el hash de la contraseña en texto plano
    def verificar_password(self, password):
        return self.__password_hash == self.__generar_hash(password)
    
    def obtener_password_hash(self):
        return self.__password_hash
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def cambiar_password(self, nuevo_password_hash):
        self.__password_hash = nuevo_password_hash

    def mostrar_datos(self):
        print(f"ID: {self.id} | Nombre: {self.nombre} | Correo: {self.correo} | Rol: {self.rol}")