import tkinter as tk
from tkinter import ttk

def saludar():
    etiqueta2.config(text="hola, " + entrada_texto.get())

root = tk.Tk()
root.title("mi primer ventana (raiz)")
root.geometry("800x600")

etiqueta = ttk.Label(root, text="nombre:", font="helvetica 20")
etiqueta.grid(row=0, column=0, padx=20, pady=20)

entrada_texto = ttk.Entry(root, font="helvetica 20")
entrada_texto.grid(row=0, column=1, padx=10, pady=20)

etiqueta2 = ttk.Label(root, font="helvetica 30",
                      background="#0099cc",
                      foreground="#f2f2f2")
etiqueta2.grid(row=1, column=0, columnspan=2)

boton = ttk.Button(root,
                   text="esto es un boton",
                   padding=10)
boton.config(command=saludar)
boton.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

check = ttk.Checkbutton(root,
                        text="aceptas los terminos?")
check.grid(row=3, column=0, columnspan=2)

opcion = tk.StringVar()
opcion.set("rojo")

r1 = ttk.Radiobutton(root, text="rojo", variable=opcion, value="rojo")
r2 = ttk.Radiobutton(root, text="verde", variable=opcion, value="verde")
r3 = ttk.Radiobutton(root, text="azul", variable=opcion, value="azul")

r1.grid(row=4, column=0)
r2.grid(row=4, column=1)
r3.grid(row=4, column=2
