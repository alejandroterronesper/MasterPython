
"""
Escribir un programa que añada valores a una lista
mientras que su longitud sea a menor a 120 
y luego mostrar la lista
Plus: usar while y for
"""


contador = 0 

lista = [0]

while contador < 120:
    contador += 1
    lista.append(contador)
    if len(lista) == 120:
        print(lista)
        print(len(lista))








#Primero crear un bucle WHILE que añada elementos a la lista

