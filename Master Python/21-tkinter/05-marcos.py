from tkinter import * 



ventana = Tk()
ventana.title("Rincón | Tumblr")
ventana.geometry("700x700")




marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)


marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="red",
    bd=12,
    relief=RAISED)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(FALSE)


texto = Label(marco, text="Anticristo")
texto.config(
    bg="red",
    fg="blue",
    font=("Gothic", 20),
    bd=3,
    )
texto.pack(anchor=CENTER, fill=Y, expand=YES)



marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="black",
    bd=12,
    relief=RAISED)
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.pack(side=TOP, anchor=N ,fill=X, expand=YES)



marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="blue",
    bd=12,
    relief=RAISED)
marco.pack(side=LEFT)


marco = Frame(marco_padre, width=250, height=250)
marco.config(bg="orange",
    bd=12,
    relief=RAISED)
marco.pack(side=RIGHT)






ventana.mainloop()