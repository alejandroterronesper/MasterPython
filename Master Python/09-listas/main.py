"""
LISTAS (arrays): coleccion de un conjunto de datos/valores
bajo un mismo nombre.
Para acceder a eso valores podemos usar un indice numerico. 

Puede ser una variable que contiene muchas variables que contiene 
un conjunto de datos
"""

#Definir lista
print("\n CON CORCHETES")
corchetes = ["dinero", "arroz"]

print(corchetes)
print("\n CON TUPLAS")
#dentro de la funcion se añade la funcion list acompañada de la tupla, los elementos no se pueden modificar
tupla = list(("Hola", "que"))
print(tupla)

print("\n Con RANGE usando tupla")
year = list(range(1998,2022))
print(year)

print("\n lista variada")
medley = ["Cañete", 4, 4.5, True]
print(medley)