## servicios/biblioteca_servicio.py

# Importamos los modelos
from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """
    Clase que contiene la lógica del sistema de biblioteca.
    Aquí se gestionan libros, usuarios, préstamos y devoluciones.
    """

    def __init__(self):

        # Diccionario donde:
        # clave -> ISBN
        # valor -> objeto Libro
        # Permite acceder rápidamente a los libros
        self.__libros_disponibles = {}

        # Diccionario para almacenar usuarios
        # clave -> ID usuario
        # valor -> objeto Usuario
        self.__usuarios = {}

        # Conjunto (set) para asegurar IDs únicos de usuarios
        self.__ids_usuarios = set()

    # GESTIÓN DE LIBROS

    def añadir_libro(self, titulo, autor, categoria, isbn):

        # Verificamos que el libro no exista
        if isbn in self.__libros_disponibles:
            print("El libro ya existe.")
            return

        # Creamos el objeto libro
        libro = Libro(titulo, autor, categoria, isbn)

        # Lo añadimos al diccionario
        self.__libros_disponibles[isbn] = libro

        print("Libro añadido correctamente.")

    def quitar_libro(self, isbn):

        # Verificamos que el libro exista
        if isbn in self.__libros_disponibles:

            # Eliminamos el libro del catálogo
            del self.__libros_disponibles[isbn]

            print("Libro eliminado.")

        else:
            print("Libro no encontrado.")

    def listar_libros(self):

        # Si no hay libros disponibles
        if not self.__libros_disponibles:
            print("No hay libros disponibles.")
            return

        # Recorremos el diccionario e imprimimos cada libro
        for libro in self.__libros_disponibles.values():
            print(libro)

    # GESTIÓN DE USUARIOS

    def registrar_usuario(self, nombre, user_id):

        # Verificamos que el ID no exista
        if user_id in self.__ids_usuarios:
            print("El usuario ya existe.")
            return

        # Creamos el usuario
        usuario = Usuario(nombre, user_id)

        # Guardamos el usuario en el diccionario
        self.__usuarios[user_id] = usuario

        # Añadimos el ID al conjunto
        self.__ids_usuarios.add(user_id)

        print("Usuario registrado.")

    def dar_baja_usuario(self, user_id):

        # Verificamos si el usuario existe
        if user_id in self.__usuarios:

            # Eliminamos el usuario
            del self.__usuarios[user_id]

            # Eliminamos el ID del set
            self.__ids_usuarios.remove(user_id)

            print("Usuario eliminado.")

        else:
            print("Usuario no encontrado.")

    # PRÉSTAMOS DE LIBROS

    def prestar_libro(self, user_id, isbn):

        # Verificamos que el usuario exista
        if user_id not in self.__usuarios:
            print("Usuario no existe.")
            return

        # Verificamos que el libro esté disponible
        if isbn not in self.__libros_disponibles:
            print("Libro no disponible.")
            return

        # Obtenemos el usuario
        usuario = self.__usuarios[user_id]

        # Obtenemos el libro
        libro = self.__libros_disponibles[isbn]

        # Añadimos el libro a la lista del usuario
        usuario.agregar_libro(libro)

        # Eliminamos el libro de disponibles
        del self.__libros_disponibles[isbn]

        print("Préstamo realizado.")

    def devolver_libro(self, user_id, isbn):

        # Verificamos que el usuario exista
        if user_id not in self.__usuarios:
            print("Usuario no existe.")
            return

        usuario = self.__usuarios[user_id]

        # Buscamos el libro en los préstamos del usuario
        for libro in usuario.get_libros_prestados():

            if libro.get_isbn() == isbn:

                # Eliminamos el libro de su lista
                usuario.devolver_libro(libro)

                # Lo volvemos a añadir al catálogo
                self.__libros_disponibles[isbn] = libro

                print("Libro devuelto correctamente.")
                return

        print("El usuario no tiene ese libro.")

    # BÚSQUEDAS

    def buscar_por_titulo(self, titulo):

        resultados = []

        # Recorremos los libros disponibles
        for libro in self.__libros_disponibles.values():

            if libro.get_titulo().lower() == titulo.lower():
                resultados.append(libro)

        return resultados

    def buscar_por_autor(self, autor):

        resultados = []

        for libro in self.__libros_disponibles.values():

            if libro.get_autor().lower() == autor.lower():
                resultados.append(libro)

        return resultados

    def buscar_por_categoria(self, categoria):

        resultados = []

        for libro in self.__libros_disponibles.values():

            if libro.get_categoria().lower() == categoria.lower():
                resultados.append(libro)

        return resultados

    # LIBROS PRESTADOS A USUARIO

    def listar_libros_usuario(self, user_id):

        if user_id not in self.__usuarios:
            print("Usuario no encontrado.")
            return []

        return self.__usuarios[user_id].get_libros_prestados()