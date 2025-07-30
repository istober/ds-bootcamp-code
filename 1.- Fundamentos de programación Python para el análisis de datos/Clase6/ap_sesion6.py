# Requerimiento 1 y 2
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

# Requerimiento 3
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_isbn(self):
        return self.__isbn

# Requerimiento 4
    def descripcion(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}"

# Requerimiento 5
class Biblioteca:
    def __init__(self):
        self.libros = []
    def agregar_libro(self, libro):
        return self.libros.append(libro)

# Requerimiento 6
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro.descripcion())

# Requerimiento 7
biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728")
libro2 = Libro("1984", "George Orwell", "978-0451524935")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

biblioteca.mostrar_libros()