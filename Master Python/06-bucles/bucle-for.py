"""
Un bucle es una estructura repititiva que si se cumple
va a repetir un bloque de codigo X cantidad de veces.
Hay dos bucles: FOR y WHILE

-FOR: ESTRUCTURA REITERATIVA QUE SE REPITE UNA CANTIDAD DE VECES. 
elemento iterable dura X, y ejecuta un bloque de instrucciones y puede ser
una LISTA, RANGO, o un dato que almacene distintos tipos de datos 

El bucle for lo que hace es que mientras que queden elementos dentro 
del elemento_iterable va a crear una variable por cada elemento que haya 
dentro de ese elemento. 
El bucle ejecutara el bloque de instrucciones hasta que el 
elemento_iterable se termine. 
ej. si tengo cinco elementos (cinco numeros) dentro de un rango,
el FOR va a ejecutar BLOQUE DE INSTRUCCIONES 5 veces, hasta que elemento_iterable se termine


for variable in elemento_iterable 
    bloque de instrucciones


"""

contador = 0

for contador in range(0,5):
    print("Voy por el  " + str(contador))

# Es un rango de cinco números (0,5), por lo que va del 0 al 4. 

"""
Mismo ejemplo pero una variable resultado
que gaurde todas las sumas de los numeros que hay dentro 
del rango. Sumar todos los numeros del rango
"""

contador = 0
resultado = 0 

for contador in range(0,10):
    print("Voy por el  " + str(contador))

    resultado += contador 
"""
lo que va a ser el resultado es sumar todos los todos. 
primero va a dar 10 vueltas, a partir del contador 0 = 0,1,2,3... 
y a su vez hace 0 + 0, 
luego pasa por el 1 --> 0 + 1, el resultado ahora vale 1
siguiente vuelta --> 1 + 2,
3 + 3,
6 + 4, 
10 + 5, 
15 + 6, 
21 + 7,
28 + 8,
36 + 9

Por cada vuelta, en un rango de 10 números, el resultado va a ser 
la adición del siguiente, así hasta terminar el rango. 
""" 
print(f"\nEl resultado es: {resultado}")


"""
ELEMENTOS DEL BUCLE FOR:
-CONTADOR 
-CONDICION 
-ELEMENTO (RANGO)
"""