# from pydantic import BaseModel


class Libro:
    isbn: str
    titulo: str
    genero: str
    portada: str
    sinopsis: str
    ejemplares: str
    prestamo_usuario: str
    fecha_prestamo: str

    def __init__(
        self,
        isbn,
        titulo,
        genero,
        portada,
        sinopsis,
        ejemplares,
        prestamo_usuario,
        fecha_prestamo,
    ):
        self.isbn = isbn
        self.titulo = titulo
        self.genero = genero
        self.portada = portada
        self.sinopsis = sinopsis
        self.ejemplares = ejemplares
        self.prestamo_usuario = prestamo_usuario
        self.fecha_prestamo = fecha_prestamo

    def __str__(self) -> str:
        return f"isbn: {self.isbn}, titulo: {self.titulo}, genero: {self.genero}, portada: {self.portada}, sinopsis: {self.sinopsis}, ejemplares: {self.ejemplares}, prestamo: {self.prestamo_usuario}, fecha de préstamo: {self.fecha_prestamo}"
