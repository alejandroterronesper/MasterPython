from genericpath import isfile
from io import open
import pathlib
import shutil 

# Abrir archivo

"""
Para importar un archivo usamos la funcion OPEN que está en el fichero IO

Para abrir el archivo usamos OPEN --> open("LE PASO DONDE ESTA EL ARCHIVO", "a+")

a+ --> es un PERMISO
"""

"""
archivo = open("14-sistema-archivo/fichero_texto.txt", "a+")

con la ruta abrimos el fichero, pero como no existia hay que crearlo

archivo = open("fichero_texto.txt", "a+")  

"""

# usando PATHLIB --> hay que concatenarlo usando el STR

ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

archivo = open(ruta, "a+")


# Escribir dentro de un archivo

archivo.write("\tManuscrito hallado en una botella\n")



# Cerrar archivo

archivo.close()


# Leer contenido del archivo --> PERMISO: r

# 1º abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"

leer = open(ruta, "r")


# Leer contenido 

contenido = leer.read()
print(contenido)


# Leer contenido y guardar en lista

lista = leer.readlines()
leer.close()

for frase in lista:
    if not frase.isnumeric():
        print("-" + frase.upper())


for frase in lista:
    lista_frase = frase.split()
    print(lista_frase)


# Copiar archivo 
"""
Coger archivo de la ruta en la que está
 y copiarlo con la ruta que queramos

"""
#archivo original
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
#archivo copiado, va a la misma carpeta
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"

# shutil.copyfile(ORIGINAL, COPIA)
shutil.copyfile(ruta_original, ruta_nueva)


#Para copiarlo a otra carpeta hay que poner la direccion

ruta_alternativa = "../07-ejercicios/fichero_copiadodeotracarpeta.txt"

shutil.copyfile(ruta_original, ruta_alternativa)


# Mover/renombrar 

ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
#se elimina el archivo fichero_copiado porque se renombra como fichero_copiado_nuevo
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"


#Asi le cambiamos de nombre al archivo
shutil.move(ruta_original,ruta_nueva)




#ARCHIVO MOVIDO A OTRA CARPETA CON NOMBRE NUEVO
ruta_original = str(pathlib.Path().absolute()) + "/fichero_copiado_NUEVO.txt"

ruta_prueba = "../07-ejercicios/fichero_copiado_NUEVO_acoplado.txt" 

shutil.move(ruta_original,ruta_prueba)



# Eliminar

import os

ruta_eliminar = str(pathlib.Path().absolute()) + "/fichero_copiadodeotracarpeta.txt"

os.remove(ruta_eliminar)

# Comprobar si existe

import os.path


print(os.path.abspath("../")) 
#--> me saca la ruta 


# Comprobar si fichero existe

ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
print(ruta_comprobar)


if os.path.isfile(ruta_comprobar):
    print("el archivo existe")
else:
    print("Pues no está")