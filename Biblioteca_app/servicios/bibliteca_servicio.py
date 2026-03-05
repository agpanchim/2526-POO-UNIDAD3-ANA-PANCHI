# servicios/biblioteca_servicio.py

from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:
    """
    Contiene la lógica del sistema de biblioteca.
    Administra libros, usuarios y préstamos.
    """

    def __init__(self):

        # diccionario obligatorio
        self.__libros_disponibles = {}

        # usuarios registrados
        self.__usuarios = {}

        # set obligatorio para IDs únicos
        self.__ids_usuarios = set()

    # LIBROS

    def añadir_libro(self, titulo, autor, categoria, isbn):

        if isbn in self.__libros_disponibles:
            print("⚠ El libro ya existe.")
            return

        libro = Libro(titulo, autor, categoria, isbn)
        self.__libros_disponibles[isbn] = libro

        print("✅ Libro añadido correctamente.")

    def quitar_libro(self, isbn):

        if isbn in self.__libros_disponibles:
            del self.__libros_disponibles[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    def listar_libros(self):

        if not self.__libros_disponibles:
            print("No hay libros disponibles.")
            return

        for libro in self.__libros_disponibles.values():
            print(libro)

    # -------------------------
    # USUARIOS
    # -------------------------

    def registrar_usuario(self, nombre, user_id):

        if user_id in self.__ids_usuarios:
            print("⚠ El usuario ya existe.")
            return

        usuario = Usuario(nombre, user_id)

        self.__usuarios[user_id] = usuario
        self.__ids_usuarios.add(user_id)

        print("✅ Usuario registrado.")

    def dar_baja_usuario(self, user_id):

        if user_id in self.__usuarios:
            del self.__usuarios[user_id]
            self.__ids_usuarios.remove(user_id)

            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # -------------------------
    # PRÉSTAMOS
    # -------------------------

    def prestar_libro(self, user_id, isbn):

        if user_id not in self.__usuarios:
            print("Usuario no existe.")
            return

        if isbn not in self.__libros_disponibles:
            print("Libro no disponible.")
            return

        usuario = self.__usuarios[user_id]
        libro = self.__libros_disponibles[isbn]

        usuario.agregar_libro(libro)

        del self.__libros_disponibles[isbn]

        print("📚 Préstamo realizado.")

    def devolver_libro(self, user_id, isbn):

        if user_id not in self.__usuarios:
            print("Usuario no existe.")
            return

        usuario = self.__usuarios[user_id]

        for libro in usuario.get_libros_prestados():

            if libro.get_isbn() == isbn:

                usuario.devolver_libro(libro)
                self.__libros_disponibles[isbn] = libro

                print("Libro devuelto correctamente.")
                return

        print("El usuario no tiene ese libro.")

    # -------------------------
    # BUSQUEDAS
    # -------------------------

    def buscar_por_titulo(self, titulo):

        resultados = []

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

    # -------------------------
    # LISTAR LIBROS DE USUARIO
    # -------------------------

    def listar_libros_usuario(self, user_id):

        if user_id not in self.__usuarios:
            print("Usuario no encontrado.")
            return []

        return self.__usuarios[user_id].get_libros_prestados()