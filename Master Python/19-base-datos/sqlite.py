#importar modulo sqlite 3 que nos permite conectar con la base de datos


import sqlite3


# Conexión 
conexion = sqlite3.connect('./19-base-datos/pruebas.db')
#al sqlite3 hay que pasarle un parametro, un fichero, que es la la BD


# Es necesario un CURSOR para la TABLA
cursor = conexion.cursor()

# Crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar (255),
    descripcion text,
    precio int(255)
);
""")

# Guardar cambios
conexion.commit()

# Insertar datos

"""
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'descripción del producto', 550)")
conexion.commit()
"""

# Brorrar registros

cursor.execute("DELETE FROM productos")
conexion.commit()


# Insertar muchos registros de golpe

productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono", "Buen telefono", 145),
    ("placa base", "Buena plaquita", 7400),
    ("Tablet 15", "Buena tablet", 300),
]

cursor.executemany("INSERT INTO  productos VALUES (null,?,?,?)", productos)
conexion.commit()



# Actualizar datos
cursor.execute("UPDATE productos set precio=4566666 WHERE precio=700")



# Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 100;")


productos = cursor.fetchall()
print(productos)
#los productos se alacenan en una TUPLA


for producto in productos:
    print("ID: ", producto[0])
    print("Título:",producto[1])
    print("Descripción:", producto[2])
    print("Precio:", producto[3])
    print("\n")



cursor.execute("SELECT * FROM productos;")
producto = cursor.fetchone()
print(producto)


# Cerrar conexión
conexion.close()