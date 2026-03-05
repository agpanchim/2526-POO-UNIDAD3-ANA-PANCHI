# modelos/libro.py

class Libro:
    """
    Representa un libro dentro del sistema de biblioteca.
    Este modelo solo almacena información del libro.
    """

    def __init__(self, titulo, autor, categoria, isbn):
        # Se usa tupla porque título y autor no deben modificarse
        self.__info = (titulo, autor)
        self.__categoria = categoria
        self.__isbn = isbn

    def get_titulo(self):
        return self.__info[0]

    def get_autor(self):
        return self.__info[1]

    def get_categoria(self):
        return self.__categoria

    def get_isbn(self):
        return self.__isbn

    def __str__(self):
        return f"{self.get_titulo()} - {self.get_autor()} | {self.__categoria} | ISBN:{self.__isbn}"