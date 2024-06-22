#Funciones dentro de otra funcion

def getnombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto
   

def getapellido(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto


# print(getnombre("Cañete"), getapellido("Cañete"))
    



#Esto es una versión desecha de lo que queremos hacer
#pues usamos dos funciones para unirlas dentro de un mismo 
#print, podemos usar una funcion dentro de una funcion

print("\nFUNCIONES DENTRO DE UNA FUNCION")

"""
Previamente hay que DEFINIR las FUNCIONES: def getnombre y def getapellido
En la siguiente FUNCION crear una VARIABLE que cotengan las FUNCIONES que queremos 
Se reutiliza cogido
"""
def getTodo(nombre, apellidos):
    texto = getnombre + " " + getapellido
    return texto

print("Daniel","Cañete")