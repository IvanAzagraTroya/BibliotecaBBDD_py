# from pydantic import BaseModel


class Usuario:
    dni: str
    nombre: str
    correo: str
    telf: str
    domicilio: str
    libros_prestados: str

    def __init__(self, dni, nombre, correo, telf, domicilio, libros_prestados):
        self.dni = dni
        self.nombre = nombre
        self.correo = correo
        self.telf = telf
        self.domicilio = domicilio
        self.libros_prestados = libros_prestados

    def __str__(self) -> str:
        return f"dni: {self.dni}, nombre: {self.nombre}, correo: {self.correo}, teléfono: {self.telf}, domicilio: {self.domicilio}, libros: {self.libros_prestados}"
