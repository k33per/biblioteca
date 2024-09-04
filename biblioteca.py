# Clase Biblioteca:
# Atributos:
# libros (list): Lista de libros en la biblioteca.
# usuarios (list): Lista de usuarios registrados en la biblioteca.
# Métodos:
# agregar_libro(libro): Añade un libro a la lista de libros de la biblioteca.
# registrar_usuario(usuario): Añade un usuario a la lista de usuarios de la biblioteca.
# prestar_libro(titulo, usuario): Permite a un usuario prestar un libro disponible por su título. Retorna True si se pudo prestar el libro, y False en caso contrario.
# devolver_libro(titulo, usuario): Permite a un usuario devolver un libro prestado por su título. Retorna True si se pudo devolver el libro, y False en caso contrario.

class Biblioteca:
    """
    Clase de Biblioteca
    """

    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, titulo, usuario) -> bool:
        for libro in self.libros:
            if libro.titulo == titulo and usuario.prestar_libro(libro):
                return True

        return False

    def devolver_libro(self, titulo, usuario):
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo and usuario.devolver_libro(libro):
                return True

        return False
