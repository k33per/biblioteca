# Clase Usuario:
# Atributos:
# nombre (str): El nombre del usuario.
# libros_prestados (list): Lista de libros que el usuario ha prestado.
# Métodos:
# prestar_libro(libro): Añade el libro a la lista de libros prestados si está disponible, y lo marca como no disponible. Retorna True si se pudo prestar el libro, y False en caso contrario.
# devolver_libro(libro): Elimina el libro de la lista de libros prestados y lo marca como disponible. Retorna True si se pudo devolver el libro, y False en caso contrario.

class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro) -> bool:
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True

        return False

    def devolver_libro(self, libro) -> bool:
        if libro in self.libros_prestados:
            libro.devolver()
            self.libros_prestados.remove(libro)
            return True

        return False
