from tkinter import *


ventana = Tk()
ventana.geometry("600x600")

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="New File")
archivo.add_command(label="New Window")
archivo.add_separator()
archivo.add_command(label="Open File")
archivo.add_command(label="Open Folder")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit)


mi_menu.add_cascade(label="File", menu=archivo)
mi_menu.add_command(label="Edit")
mi_menu.add_command(label="Selection")



ventana.mainloop()