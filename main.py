# Descripción
# Vas a implementar un sistema de gestión de una biblioteca que permita registrar libros y usuarios, y manejar el préstamo y la devolución de libros. Además, debes escribir pruebas unitarias para asegurar que las funcionalidades del sistema funcionan correctamente.
# Requisitos del Sistema
# Clase Libro:
# Atributos:
# titulo (str): El título del libro.
# autor (str): El autor del libro.
# disponible (bool): Indica si el libro está disponible para préstamo.
# Métodos:
# prestar(): Marca el libro como no disponible si está disponible, y retorna True; de lo contrario, retorna False.
# devolver(): Marca el libro como disponible.
# Clase Usuario:
# Atributos:
# nombre (str): El nombre del usuario.
# libros_prestados (list): Lista de libros que el usuario ha prestado.
# Métodos:
# prestar_libro(libro): Añade el libro a la lista de libros prestados si está disponible, y lo marca como no disponible. Retorna True si se pudo prestar el libro, y False en caso contrario.
# devolver_libro(libro): Elimina el libro de la lista de libros prestados y lo marca como disponible. Retorna True si se pudo devolver el libro, y False en caso contrario.
# Clase Biblioteca:
# Atributos:
# libros (list): Lista de libros en la biblioteca.
# usuarios (list): Lista de usuarios registrados en la biblioteca.
# Métodos:
# agregar_libro(libro): Añade un libro a la lista de libros de la biblioteca.
# registrar_usuario(usuario): Añade un usuario a la lista de usuarios de la biblioteca.
# prestar_libro(titulo, usuario): Permite a un usuario prestar un libro disponible por su título. Retorna True si se pudo prestar el libro, y False en caso contrario.
# devolver_libro(titulo, usuario): Permite a un usuario devolver un libro prestado por su título. Retorna True si se pudo devolver el libro, y False en caso contrario.
#
# Pruebas Unitarias(20 pts +)
# Debes escribir pruebas unitarias para validar las siguientes funcionalidades:
# Agregar Libro: Verifica que un libro se pueda agregar a la biblioteca.
# Registrar Usuario: Verifica que un usuario se pueda registrar en la biblioteca.
# Prestar Libro Disponible: Verifica que un libro disponible se pueda prestar a un usuario.
# Prestar Libro No Disponible: Verifica que un libro no disponible no se pueda prestar.
# Devolver Libro Prestado: Verifica que un libro prestado se pueda devolver.
# Devolver Libro No Prestado: Verifica que un libro que no ha sido prestado no se pueda devolver.

from libro import Libro
from biblioteca import Biblioteca
from usuario import Usuario
import unittest


class UnitTestBiblioteca(unittest.TestCase):
    def setUp(self) -> None:
        self.biblioteca = Biblioteca()
        self.libro = Libro("100 anos de soledad", "Gabo")
        self.usuario = Usuario("Pedro")

    def test_agregar_libro(self):
        self.biblioteca.agregar_libro(self.libro)
        self.assertIn(self.libro, self.biblioteca.libros)

    def test_registrar_usuario(self):
        self.biblioteca.registrar_usuario(self.usuario)
        self.assertIn(self.usuario, self.biblioteca.usuarios)

    def test_prestar_libro_disponible(self):
        self.biblioteca.agregar_libro(self.libro)
        self.biblioteca.registrar_usuario(self.usuario)
        self.assertTrue(self.biblioteca.prestar_libro("100 anos de soledad", self.usuario))

    def test_prestar_libro_no_disponible(self):
        self.libro.disponible = False
        self.biblioteca.agregar_libro(self.libro)
        self.biblioteca.registrar_usuario(self.usuario)
        self.assertFalse(self.biblioteca.prestar_libro("100 anos de soledad", self.usuario))


if __name__ == "__main__":
    unittest.main()
