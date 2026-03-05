# modelos/libro.py

class Libro:
    """
    Clase que representa un libro dentro del sistema de biblioteca.
    Este modelo únicamente almacena la información del libro.
    No contiene lógica del negocio, ya que esa responsabilidad
    pertenece a la capa de servicios.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        # Se usa tupla porque título y autor no deben modificarse (inmutables)
        self.__info = (titulo, autor)
        # Categoría del libro
        self.__categoria = categoria
        # ISBN funciona como identificador único del libro
        self.__isbn = isbn

    # Métodos GET (encapsulamiento)

    # Devuelve el título del libro
    def get_titulo(self):
        return self.__info[0]

    # Devuelve el autor del libro
    def get_autor(self):
        return self.__info[1]

    # Devuelve la categoría
    def get_categoria(self):
        return self.__categoria

    # Devuelve el ISBN
    def get_isbn(self):
        return self.__isbn

    # Representación en texto del objeto
    # Permite imprimir el libro fácilmente
    def __str__(self):
        return f"{self.get_titulo()} - {self.get_autor()} | {self.__categoria} | ISBN:{self.__isbn}"