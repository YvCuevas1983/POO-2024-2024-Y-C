import tkinter as tk
from tkinter import messagebox

# Función para agregar elementos a la lista
def agregar_dato():
    dato = entrada_texto.get()
    if dato:
        lista_datos.insert(tk.END, dato)  # Agrega el texto al final de la lista
        entrada_texto.delete(0, tk.END)  # Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)  # Borra todos los elementos de la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=10)

# Campo de texto
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=5)

# Botón para agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar la ventana principal
ventana.mainloop()