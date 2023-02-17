import tkinter
from tkinter import ttk
from menu import menu


# Se pueden introducir el número de alumnos que se desea vía consola
def main():
    print("--- Bienvenido a la biblioteca ---")
    menu()


# window = tkinter.Tk()
# window.title("Lista de libros")
# escogido = tkinter.StringVar()
# listbox = tkinter.Listbox(window)
# escogido.set(None)

# for elem in lista_libros:
#    listbox.insert(tkinter.END, elem)
# listbox.pack()

# def add():
#    new_elem = lista_libros.get()
#    lista_libros.append(new_elem)
#    listbox.insert(tkinter.END, new_elem)

# window.mainloop()

if __name__ == "__main__":
    main()
