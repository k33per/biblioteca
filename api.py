from typing import List

from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca
from fastapi import FastAPI, HTTPException

app = FastAPI()
biblioteca = Biblioteca()


def encontrar_usuario(nombre_usuario: str):
    usuario = next((usuario for usuario in biblioteca.usuarios if usuario.nombre == nombre_usuario), None)

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado en la biblioteca")
    else:
        return usuario


@app.post("/libros")
def agregar_libro(titulo: str, autor: str):
    libro = Libro(titulo, autor)
    biblioteca.agregar_libro(libro)
    return {"message": f"Libro {titulo} agregado exitosamente"}


@app.get("/libros", response_model=List[dict])
def retornar_libros():
    return [{
        "titulo": libro.titulo,
        "autor": libro.autor,
        "disponibilidad": libro.disponible
    } for libro in biblioteca.libros]


@app.post("/usuarios")
def agregar_usuario(nombre: str):
    usuario = Usuario(nombre)
    biblioteca.registrar_usuario(usuario)
    return {"message": f"Usuario {nombre} registrado exitosamente"}


@app.post("/prestamos/")
def prestar_libro(titulo: str, nombreUsuario: str):
    usuario = encontrar_usuario(nombreUsuario)

    if biblioteca.prestar_libro(titulo, usuario):
        return {"message": f"El libro {titulo} ha sido prestado exitosamente al usuario {nombreUsuario}"}

    raise HTTPException(status_code=404,
                        detail=f"ERROR. El libro {titulo} no ha podido ser prestado al usuario {nombreUsuario}")


@app.post("/devoluciones/")
def devolver_libro(titulo: str, nombreUsuario: str):
    usuario = encontrar_usuario(nombreUsuario)

    if biblioteca.devolver_libro(titulo, usuario):
        return {"message": f"El libro {titulo} ha sido devuelto exitosamente a la biblioteca"}

    raise HTTPException(status_code=404,
                        detail=f"ERROR. El libro {titulo} no ha podido ser devuelto a la biblioteca")
