from tkinter import *


ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="COSITAS")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Gothic", 20)
)
encabezado.grid(row=0, column=0, columnspan=6, sticky=W)



# Botones check
def mostrarProfesion():
    texto = ""

    if web.get():
        texto += "Con un ojo abierto    "
    
    if mobil.get():
        if web.get():
            texto += " con dos cojones"
        else:
            texto += "a robah "

    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
        )


web = IntVar()
mobil = IntVar()



Label(ventana, text="Que haces, dime lo que haces").grid(row=1, column=0)
Checkbutton(
    ventana, 
    text="acoplar",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
    ).grid(row=2, column=0)
Checkbutton(
    ventana, 
    text="robar",
    variable=mobil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
    ).grid(row=3, column=0)


mostrar = Label(ventana)
mostrar.grid(row=4, column=0)


# Radio Buttons
def marcar():
    marcado.config(text=opcion.get())




opcion = StringVar()
opcion.set(None)

Label(ventana, text="Cual es tu genero").grid(row=5)

Radiobutton(
    ventana, 
    text="maricon",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6)


Radiobutton(
    ventana, 
    text="puta",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)



# Option Menu
def seleccionar():
    seleccionado.config(text=respuesta.get())

respuesta = StringVar()
respuesta.set("Platano ")

Label(ventana, text="Selecciona una opcion").grid(row=5, column=1)

select = OptionMenu(ventana, respuesta, "Platano ", "Melones", "Kiwis" )
select.grid(
    row=6,
    column=1

)

Button(ventana, text="Ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)



ventana.mainloop()