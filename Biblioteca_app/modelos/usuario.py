# modelos/usuario.py

class Usuario:
    """
    Representa un usuario registrado en la biblioteca.
    """

    def __init__(self, nombre, user_id):
        # Nombre del usuario
        self.__nombre = nombre
        # Identificador único del usuario
        self.__user_id = user_id
        # Lista que almacena los libros prestados
        # Se usa LISTA
        self.__libros_prestados = []  # lista obligatoria

    # Devuelve el nombre del usuario
    def get_nombre(self):
        return self.__nombre

    # Devuelve el ID del usuario
    def get_user_id(self):
        return self.__user_id

    # Devuelve la lista de libros prestados
    def get_libros_prestados(self):
        return self.__libros_prestados

    # Añade un libro a la lista de préstamos
    def agregar_libro(self, libro):
        self.__libros_prestados.append(libro)

    # Elimina un libro cuando es devuelto
    def devolver_libro(self, libro):
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)

    # Representación en texto del usuario
    def __str__(self):
        return f"Usuario: {self.__nombre} | ID: {self.__user_id}"