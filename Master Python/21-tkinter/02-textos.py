from cgitb import text
from tkinter import *


ventana = Tk()
ventana.geometry("666x666")

# Keywords arguments -- > text 

texto = Label(ventana,text="Bienvenidos al Infierno")
texto.config(
    fg="red",
    bg="black",
    padx=20,
    pady=20,
    font=("Gothic", 30)
)
# Hay que ejecutar al texto dentro de la ventana
texto.pack()

def pruebas(nombre, apellidos, pais):
    return f"Bienvenido {nombre} {apellidos}, me di cuenta de que eres de {pais}"




texto = Label(ventana,text=pruebas(apellidos="Terror",nombre="Señor", pais="Lepe"))
texto.config(
    height=6,
    bg="Blue",
    font=("Gothic", 18),
    cursor="spider"
)
texto.pack(anchor=SE)
# El movimiento del texto (ANCHOR) se indica dentro del PACk



ventana.mainloop()