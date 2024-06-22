from struct import pack
from tkinter import *

ventana = Tk()

ventana.config(
    bd=50,

)


def getDato():
    resultado.set(dato.get())

    if len(resultado.get()) >=1: 
        texto_recogido.config(
            bg="green",
            fg="white"
        )


# Para recoger datos usamos la variable StringVar()
dato = StringVar()
resultado = StringVar()

Label(ventana, text="Pon aqui algo").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)


Label(ventana, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)
texto_recogido.pack(anchor=NW)


Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)



ventana.mainloop()