"""
Crear un programa que tenga:
- Ventana
- Tamaño fijo
- No redimensionable
- Un menu (Inicio, añadir, información, salir)
- Diferentes pantallas
- Formulario de añadir producto
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
- Opcion de salir
"""

from tkinter import * 
from tkinter import ttk

ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(500, 500)
ventana.title("La hemeroteca de Eustaquio")

# Ventana no redimensionable 
ventana.resizable(0,0)



# Pantallas

def home():
    # Montar pantalla 
    home_label.config(
        fg="white",
        bg="black",
        font=("Gothic", 30),
        padx=190,
        pady=20
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=2)

    # Listar productos 
    """
    for product in products: 
        if len(product) == 3:
            product.append("added")
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text="-----------------").grid()
    """
    for product in products: 
        if len(product) == 3:
            product.append("added")
            products_box.insert('', 0, text=product[0], values= (product[1]))

    # Ocultar otras pantallas
    
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()


    return True


def add():
    # Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Gothic", 30),
        padx=110,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    # Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_descripcion_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_descripcion_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_descripcion_entry.config(
        width=30, 
        height=5, 
        font=("Gothic", 12), 
        padx=15, 
        pady=15 
        )


    add_separator.grid(row=4, column=1)


    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        padx=15,
        pady=5,
        bg="black",
        fg="white"
    )


    # Ocultar otras pantallas 
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()



    return True

def info():
    info_label.config(
    fg="white",
    bg="black",
    font=("Gothic", 30),
    padx=140,
    pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)

    home_label.grid_remove()
    products_box.grid_remove()
    add_frame.grid_remove()
    add_label.grid_remove()
    

    return True

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_descripcion_entry.get("1.0", "end-1c")
    ]) 

    name_data.set("")
    price_data.set("")
    add_descripcion_entry.delete("1.0", END)

    home()

    

# Variables importantes
products = []
name_data = StringVar()
price_data = StringVar()

# Definir campos de pantallas INICIO
home_label =  Label(ventana, text="Inicio")
#products_box = Frame(ventana, width=250)

Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text='Producto', anchor=W)
products_box.heading("#1", text='Precio', anchor=W)

# Definir campos de pantallas AÑADIR
add_label =  Label(ventana, text="Añadir producto")


# Campos del formulario
add_frame = Frame(ventana)
add_name_label = Label(add_frame, text="Nombre:  ")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_descripcion_label = Label(add_frame, text="Descripción:   ")
add_descripcion_entry = Text(add_frame)

add_separator = Label(add_frame)

# Botón

boton = Button(add_frame, text="Guardar", command=add_product)

# Definir campos de pantallas INFORMACION
info_label =  Label(ventana, text="Información")
data_label = Label(ventana, text="Sueños Nigeria 2015")



# Cargar pantalla inicio
home()

# Creación de menu
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)


# Cargar menu

ventana.config(menu=menu_superior)



ventana.mainloop()