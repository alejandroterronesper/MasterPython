import os, shutil

# Crear carpeta/directorio 

"""
1-Comprobar que la carpeta existe
2- En el caso de que no existiera,
es necesario crear --> os.mkdir 
"""
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe la caperta")





# Copiar/mover carpeta/directorio 
"""
ruta_original =  "./mi_carpeta"

ruta_nueva =  "./mi_carpeta_copiada" 

shutil.copytree(ruta_original,ruta_nueva)

"""


# Eliminar carpeta/directorio 

"""
os.rmdir('./mi_carpeta_copiada')
"""

# Listar archivos dentro de la carpeta


print("Se va a mostrar por pantalla los archivos:   ")

contenido = os.listdir("./mi_carpeta")

for fichero in contenido:
    print("Fichero: " + fichero)

