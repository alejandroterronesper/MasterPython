"""
Escribir un programa que añada valores a una lista
mientras que su longitud sea a menor a 120 
y luego mostrar la lista
Plus: usar while y for
"""



valores = [0]
recorrido = 0

#tengo que crear un bucle que por cada vez que recorra la lista, le añada un valor
#luego una condicion para que este bucle se detenga cuando la longitud sea 120

print("\tCON FOR")

for recorrido in valores:
    valores 
    recorrido += 1 
    valores.append(recorrido)
    if len(valores) == 120:
        print(valores)
        print(len(valores))
    
#bucle creado con for para añadir elementos a la lista
     
contador = 0 

lista = [0]

print("\t\nCON WHILE")

while contador < 120:
    contador += 1
    lista.append(contador)
    if len(lista) == 120:
        print(lista)
        print(len(lista))




