"""
CREAR UNA LISTA QUE CONTENGA 8 NUMEROS ENTEROS
1º Recorrerla y mostrarla
2º Ordenarla y mostrarla
3º Mostrar su longitud
4º Buscar algun elemento dentro de la lista en base
a lo que el usuario nos pida por teclado
"""

numeros = [1,3,4,7,58,45,9,5]
print(numeros)
print("")
print("RECORRER LISTA")
#LO HACEMOS MEDIANTE BUCLE FOR
print("")
for mostrar in numeros:
    print(mostrar)
print("")
print("ORDENAR LISTA")


numeros.sort()

print(f"Lista ordenada: {numeros}")


print("SU LONGITUD")
print(len(numeros))


print("\nBuscar elemento dentro de la lista en base a lo que nos pida el usuario")
pregunta = input("¿Qué tipo de número quieres mostrar?:  ")

if pregunta == "par":
    for datos in numeros:
        if datos % 2 == 0:
            print(f"Los numeros pares son:  {datos}")
else:
    if pregunta == "impar":
        for datos in numeros:
            if datos % 2 != 0:
             print(f"Los numeros impares son:  {datos}")

#MAL PLANTEADO


print("FUNCION QUE RECOJA LA LISTA Y LA DEVUELVA EN STRING")

#le paso a la funcion un parametro
def numeritos(lista):
    resultado = ""

    for prueba in lista:
        resultado += "elemento  " + str(prueba)
        resultado += "\n"
    return resultado

#por cada vuelta que de prueba hay que ir concatenarle la lista numeros
print(numeritos(numeros))


#LISTA ORDENADA PERO DEVUELTA EN STRING
numeros.sort()

print(numeritos(numeros))


print("\nBuscar elemento dentro de la lista en base a lo que nos pida el usuario")
#Se refiere a BUSCAR UN NUMERO DENTRO DE LA LISTA

pregunta = int(input("Dime el número:   "))

#tenemos que comprar que el nuevo que entra es un NUMERO ENTERO
#para ello creamos una variable que guarde el valor y a traves de la
# funcion isistance(variable, INT) compruebe que es un ENTERO
comprobar = isinstance(pregunta, int)

while not comprobar or pregunta <= 0:
    pregunta = int(input("Dime el número:   "))
else:
    print(f"Introdujiste el: {pregunta}")

#con este bucle nos aseguremos la PRIMERA CONDICION que sea ENTERO
#si lo pasa, creamos OTRA VARIABLE QUE BUSQUE EL NUMERO

search = numeros.index(pregunta)
#con la funcion index te busca en que indice se encuentra el numero
# y lo guarda en la variable SEARCH
print(f" El numero {pregunta} esta en el indice {search}")