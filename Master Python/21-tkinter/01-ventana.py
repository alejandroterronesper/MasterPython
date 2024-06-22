# Tkinter
# Modulo para crear interfaces graficas de usuario


# Importamos el modulo


from tkinter import * 
import os.path


class Programa: 

    def __init__(self):
        self.title = "Las lagrimas de ULTRATUMBA"
        self.icon = './imagenes/imagen1.ico'
        self.icon_alt = './21-tkinter/imagenes/imagen1.ico'
        self.size = "770x470"
        self.resizable = False

    def cargar(self):
        # Crear una ventana raiz
        ventana = Tk()
        self.ventana = ventana

        # Añadir titulo de la ventana

        ventana.title(self.title)


        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon) 

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt) 


        # Añadir icono de la ventana, añadir la ruta

        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()


        # Cambiar tamaño de la ventana --> .geomtry
        ventana.geometry(self.size)


        # Bloquear tamaño de la ventana --> .resizable(VERTICAL, HORIZONTAL) 0 = bloquear
        if self.resizable: 
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)




        # Para que arranque la ventana
        # Hay que usar el metodo mainloop


        

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
         # Arrancar y mostrar ventana hasta que se cierre
        self.ventana.mainloop()

# Instanciar mi programa

programa = Programa()
programa.cargar()
programa.addTexto("Propicias noches, seres del inframundo")
programa.addTexto(666)
programa.mostrar()