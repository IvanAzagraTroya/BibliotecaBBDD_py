import sqlite3
from libro import Libro
from usuario import Usuario
from datetime import datetime

conn = sqlite3.connect("biblioteca.db", isolation_level=None)
cursor = conn.cursor()
exits = False
lista_libros = {}
libros_cogidos = []
libro = Libro("", "", "", "", "", "", "", "")


def introduce_libro():
    libro.isbn = input("Introduce el isbn")
    libro.titulo = input("introduce el titulo")
    libro.genero = input("Introduce el genero")
    libro.portada = input("Cómo piensas introducir una portada???")
    libro.sinopsis = input("Introduce la sinopsis")
    libro.ejemplares = input("Introduce número de ejemplares")
    libro.prestamo_usuario = Usuario.dni = input("Introduce el dni del usuario")
    libro.fecha_prestamo = datetime.now()  # .strftime()

    lista_libros.clear()
    cursor.execute(
        "CREATE TABLE if not exists Libros (isbn TEXT, titulo TEXT, genero TEXT, portada TEXT, sinopsis TEXT, ejemplares TEXT, prestamo_usuario TEXT, fecha_prestamo TEXT)"
    )
    query = """INSERT INTO Libros values (?, ?, ?, ?, ?, ?, ?, ?)"""

    cursor.execute(
        query,
        (
            libro.isbn,
            libro.titulo,
            libro.genero,
            libro.portada,
            libro.sinopsis,
            libro.ejemplares,
            libro.prestamo_usuario,
            libro.fecha_prestamo,
        ),
    )
    get_libros()
    escritura_libros_txt()

    salir = input("Desea salir? Pulsa Y")
    if salir == "Y":
        menu()
    else:
        introduce_libro()


usuario = Usuario("", "", "", "", "", "")


def get_libros():
    try:
        libro = Libro("", "", "", "", "", "", "", "")
        query = "SELECT * FROM Libros"
        cursor.execute(query)
        libros_db = cursor.fetchall()

        for row in libros_db:
            libro.isbn = row[0]
            libro.titulo = row[1]
            libro.genero = row[2]
            libro.portada = row[3]
            libro.sinopsis = row[4]
            libro.ejemplares = row[5]
            libro.prestamo_usuario = row[6]
            libro.fecha_prestamo = row[7]

            lista_libros[libro.isbn] = libro
            print(libro, "\n")

    except sqlite3.Error as error:
        print("Ha habido un error al obtener los datos:", error)
        menu()


def introduce_usuario():
    usuario.dni = input("Introduce el dni")
    usuario.nombre = input("Introduce un nombre")
    usuario.correo = input("Introduce un correo electrónico")
    usuario.telf = input("Introduce el número de teléfono")
    usuario.domicilio = input("Introduce una dirección")
    usuario.libros_prestados = ""

    cursor.execute(
        "CREATE TABLE if not exists Usuarios (dni TEXT, nombre TEXT, correo TEXT, telefono TEXT, domicilio TEXT, libros_prestados TEXT)"
    )
    query = """INSERT INTO Usuarios values (?, ?, ?, ?, ?, ?)"""

    cursor.execute(
        query,
        (
            usuario.dni,
            usuario.nombre,
            usuario.correo,
            usuario.telf,
            usuario.domicilio,
            usuario.libros_prestados,
        ),
    )

    escritura_usuarios_txt()

    salir = input("Desea salir? Pulsa Y")
    if salir == "Y":
        menu()
    else:
        introduce_usuario()


def escritura_usuarios_txt():
    f = open("usuarios.txt", "at")
    f.write(str(usuario) + "\n")
    f.close()


def escritura_libros_txt():
    f = open("libros.txt", "at")
    f.write(str(libro) + "\n")
    f.close()


def elimina_usuario():
    id = input("Introduzca el dni del usuario que desea borrar: ")
    query = "DELETE FROM Usuarios WHERE dni = (?)"
    cursor.execute(query, (id,))
    print("--- Delete hecho, mostrando tabla actualizada ---")
    get_usuarios()
    menu()


def elimina_libro():
    id = input("Introduzca el isbn del libro que desea borrar: ")
    query = "DELETE FROM Libros WHERE isbn = (?)"
    cursor.execute(query, (id,))
    print("--- Delete hecho, mostrando tabla actualizada ---")
    get_libros()
    menu()


def prestamo_libros():
    lista_libros.clear()
    get_libros()
    get_usuarios()
    print("------------------------------------------")
    eleccion = input("Elige un libro/s para tomar prestado por su isbn:")
    id = input("Introduce el dni del usuario: ")
    if eleccion in lista_libros.keys():
        libros = lista_libros.get(eleccion)
    else:
        print("La opción seleccionada no es válida.")
        menu()

    query = "UPDATE Usuarios SET libros_prestados = ? WHERE dni = ?"
    l = str(libros)
    cursor.execute(query, (l, id))
    query = "UPDATE Libro SET prestamo_usuario = 'Unavailable' WHERE isbn = (?)"
    cursor.execute(query, (eleccion))
    menu()


def devolver_libro():
    get_usuarios()
    get_libros()
    id = input("Introduzca el dni del usuario: ")
    eleccion = input("Introduzca el isbn: ")
    query = "UPDATE Libros SET prestamo_usuario = 'Available' WHERE isbn = (?)"
    cursor.execute(query, (eleccion,))
    query = "UPDATE Usuario SET libros_prestados = '' WHERE dni = (?)"
    cursor.execute(query, (id,))
    print("--- Devolución realizada, mostrando tabla actualizada ---")
    consultar_prestamos()
    get_libros()

    menu()


def get_usuarios():
    try:
        usuario = Usuario("", "", "", "", "", "")
        query = "SELECT * FROM Usuarios"
        cursor.execute(query)
        usuarios_db = cursor.fetchall()

        for row in usuarios_db:
            usuario.dni = row[0]
            usuario.nombre = row[1]
            usuario.correo = row[2]
            usuario.telf = row[3]
            usuario.domicilio = row[4]
            usuario.libros_prestados = row[5]

            print(usuario, "\n")

    except sqlite3.Error as error:
        print("Ha habido un error al obtener los datos", error)
        menu()


def consultar_prestamos():
    try:
        get_usuarios()
        id = input("Introduzca el dni del usuario que desea consultar")
        usuario = Usuario("", "", "", "", "", "")
        query = "SELECT libros_prestados FROM Usuarios WHERE dni = "
        cursor.execute(query, (id,))
        usuarios_db = cursor.fetchall()

        for row in usuarios_db:
            usuario.libros_prestados = row[0]

            print("préstamos: ", usuario.libros_prestados, "\n")
    except sqlite3.Error as error:
        print("Ha habido un error al obtener los datos", error)
        menu()


def menu():
    cursor = conn.cursor()
    print(
        """
    1. Alta de socio
    2. Baja de socio
    3. Alta de libro
    4. Baja de libro
    5. Prestar libro
    6. Devolver libro
    7. Consultar libros
    8. Consultar usuarios
    9. Consultar prestamos
    0. Salir"""
    )

    selec = int(input("Introduzca su elección"))
    if selec == 1:
        introduce_usuario()
    if selec == 2:
        elimina_usuario()
    if selec == 3:
        introduce_libro()
    if selec == 4:
        elimina_libro()
    if selec == 5:
        prestamo_libros()
    if selec == 6:
        devolver_libro()
    if selec == 7:
        get_libros()
    if selec == 8:
        get_usuarios()
    if selec == 9:
        consultar_prestamos()
    if selec == 0:
        cursor.close()
        conn.close()
        exit(0)
