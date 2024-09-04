# Clase Libro:
# Atributos:
# titulo (str): El título del libro.
# autor (str): El autor del libro.
# disponible (bool): Indica si el libro está disponible para préstamo.
# Métodos:
# prestar(): Marca el libro como no disponible si está disponible, y retorna True; de lo contrario, retorna False.
# devolver(): Marca el libro como disponible.

class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self) -> bool:
        if self.disponible:
            self.disponible = False
            return True

        return False

    def devolver(self):
        self.disponible = True
