from tkinter import *
from tkinter import messagebox as MessageBox


ventana = Tk()
ventana.config(bd=70)


def sacarAlerta():
    MessageBox.showerror("", "Te dije que no pulsar.")



Button(ventana, text="No pulsar", command=sacarAlerta).pack()




def Salir(nombre):
    resultado = MessageBox.askquestion("Salir", "Te vas?")

    if resultado != "Yes":
        MessageBox.showinfo("Hasta luego, Lucas", f"Farewell, {nombre}")
        ventana.destroy()



Button(ventana, text="saliendo", command=lambda: Salir("Satan")).pack()



ventana.mainloop()