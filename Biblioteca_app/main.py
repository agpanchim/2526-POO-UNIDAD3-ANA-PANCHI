# Importamos la capa de servicios

from servicios.biblioteca_servicio import BibliotecaServicio

# Función que muestra el menú del sistema
def menu():

    print("\n       BIBLIOTECA DIGITAL       ")
    print("1. Añadir libro")
    print("2. Registrar usuario")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro por título")
    print("6. Listar libros disponibles")
    print("7. Listar libros de usuario")
    print("8. Salir")


def main():

    # Creamos el objeto que controla el sistema
    biblioteca = BibliotecaServicio()

    # Bucle principal del programa
    while True:

        menu()

        opcion = input("Seleccione una opción: ")

        # AÑADIR LIBRO
        if opcion == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            biblioteca.añadir_libro(titulo, autor, categoria, isbn)

        # REGISTRAR USUARIO
        elif opcion == "2":

            nombre = input("Nombre: ")
            user_id = input("ID usuario: ")

            biblioteca.registrar_usuario(nombre, user_id)

        # PRESTAR LIBRO
        elif opcion == "3":

            user_id = input("ID usuario: ")
            isbn = input("ISBN libro: ")

            biblioteca.prestar_libro(user_id, isbn)

        # DEVOLVER LIBRO
        elif opcion == "4":

            user_id = input("ID usuario: ")
            isbn = input("ISBN libro: ")

            biblioteca.devolver_libro(user_id, isbn)

        # BUSCAR LIBRO
        elif opcion == "5":

            titulo = input("Título a buscar: ")

            resultados = biblioteca.buscar_por_titulo(titulo)

            for libro in resultados:
                print(libro)

        # LISTAR LIBROS DISPONIBLES
        elif opcion == "6":

            biblioteca.listar_libros()

        # LIBROS PRESTADOS
        elif opcion == "7":

            user_id = input("ID usuario: ")

            libros = biblioteca.listar_libros_usuario(user_id)

            for libro in libros:
                print(libro)

        # SALIR
        elif opcion == "8":

            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


# Punto de entrada del programa
if __name__ == "__main__":
    main()