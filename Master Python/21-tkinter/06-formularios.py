from tkinter import * 


ventana = Tk()
ventana.geometry("700x400")
ventana.title("Formularios para vender alma al diablo | Rincón Tumblr")

# Hacer encabezado

encabezado = Label(ventana, text=" Death Note Pad | Rincón Tumblr ")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Gothic", 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)


# Label para el campo (nombre)

label = Label(ventana, text="Añada su victima")
label.grid(row=1, column=0, padx=5, pady=5)

# Campo de texto (nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky= W,padx=5, pady=5)
campo_texto.config(justify="left", state="normal")





# Label para el campo (apellidos)

label = Label(ventana, text="Añada sus apellidos")
label.grid(row=2, column=0,  padx=5, pady=5)

# Campo de texto (apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky= W,padx=5, pady=5)
campo_texto.config(justify="left", state="normal")


# Label para el campo (descripción)

label = Label(ventana, text="Descripción")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)


# Crear campo de texto grande (descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    state="normal",
    width=30, 
    height=5, 
    font=("Gothic",12),
    padx=15,
    pady=15
)



# Crear botones
Label(ventana).grid(row=4, column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=10, pady=10, bg="black", fg="white")

ventana.mainloop()