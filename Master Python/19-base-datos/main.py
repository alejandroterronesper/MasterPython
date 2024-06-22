import mysql.connector


# Conexión 

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd ="",
    database = "master_python"
    
)


# Comprobar conexion 
#print(database)



# Base de datos

# Cursor 
cursor = database.cursor(buffered=True)

# Crear base de datos 
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# Comprobar si una base de datos existe 
cursor.execute("SHOW DATABASES")


for bd in cursor:
    print(bd)
"""

# Crear tablas
#Aparece en mi BD de MySQL
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id) 
)
""")


# Comprobar tabla en código
#cursor.execute("SHOW TABLES")


#for table in cursor:
#    print(table)


# Insertar datos 

#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")


# Insertar datos de manera masiva 
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Moto', 'Chula', 4564),
    ('Cohete', 'grande', 45645),
    ('cañete', 'destructor', 5000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
database.commit()


# Leer tablas

cursor.execute("SELECT * FROM vehiculos")
result = cursor.fetchall()

print("\nAqui estan mis reyes ")
for coche in result:
    print(coche[1], coche [2], coche[3])

# SACAR 1ª FILA DE LA TABLA --> fetchone
cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone



# Borrar REGISTROS de una TABLA

cursor.execute("DELETE FROM vehiculos WHERE marca = 'cañete' ")
database.commit()


# Mostrar que ha borrado

print(cursor.rowcount, "eliminada")


# Actualizar 
cursor.execute("UPDATE vehiculos SET modelo='acople' WHERE marca='Opel'")
database.commit()
print(cursor.rowcount, "se actualizo")
