"""
Proyecto Python y Mysql:

Abrir un asistente que pregunte varias cosas -->
- Login o registro.
- Si me registro, se crea un usuario en BASE DE DATOS.
- Si me conecto(login), identifica al USER y hará preguntas.
- Crear nota, mostrar notas, borrarlas. 

"""
#Se importa el modulo de acciones
from usuarios import acciones



# Definir BBDD con MYSQL
# Cuando se abra el programa tiene que ofrecernos las diferentes acciones

print("""
Acciones disponibles:
    - Registro
    - Login
""")

#Instaciamos la clase
hazEl = acciones.Acciones()

accion = input("Dime que quieres hacer: ")

# Para que IF y ELIF no queden vacios, venemos que importar el paquete de ACCIONES
if accion == "registro":
    hazEl.registro()    

elif accion == "login":
    hazEl.login()
    

