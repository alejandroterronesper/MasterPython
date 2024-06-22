from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()

ventana.geometry("700x500")


Label(ventana, text="Hola aqui").pack(anchor=W)

imagen = Image.open('./21-tkinter/imagenes/imagen.png')
render = ImageTk.PhotoImage(imagen)

# Cargar imagen dentro de un Label 

Label(ventana, image=render).pack(anchor=E)

ventana.mainloop()