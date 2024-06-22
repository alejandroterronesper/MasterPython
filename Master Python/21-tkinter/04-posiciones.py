from cgitb import text
from tkinter import *


ventana = Tk()
#ventana.geometry("666x666")


# --------------------------------------------------

texto = Label(ventana,text="Bienvenidos al INFIERNO")
texto.config(
    fg="red",
    bg="black",
    padx=20,
    pady=20,
    font=("Gothic", 30)
)

texto.pack(side=TOP)

# --------------------------------------------------

texto = Label(ventana,text= "Soy el Señor Terror")
texto.config(
    height=6,
    bg="Blue",
    font=("Gothic", 18),
    cursor="spider"
)
texto.pack(side=TOP, fill=X, expand=YES) 



# --------------------------------------------------

texto = Label(ventana,text= "666")
texto.config(
    height=6,
    bg="Red",
    font=("Gothic", 18),
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)



# --------------------------------------------------

texto = Label(ventana,text= "hehe")
texto.config(
    height=6,
    bg="Yellow",
    font=("Gothic", 18),
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)




ventana.mainloop()