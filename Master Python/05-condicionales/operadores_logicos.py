print("\tOperadores lógicos")
"""
Vamos a ver los operadores lógicos:

and --> y
not --> no
or  --> or
!   --> negación

Hemos visto como hacer una condición con el IF,
ahora vamos a ver como hacer varias condiciones dentro de él. 
Para agregar una segunda condición se introduce
el OPERADOR LOGICO "AND". 
"""

edad_minima = 18
edad_maxima = 65
edad_real = int(input("¿Qué edad tienes?    "))

if edad_real >= 18 and edad_real <= 65:
    print("Tiene la edad para trabajar.")
else:
    print("No tiene edad para trabajar.")
print(" ")
print("\tOTRO EJEMPLO DE OPERADOR LÓGICO JUNTOA  LOS DE COMPARACIÓN")

pais = input("¿De qué parte de Antequera eres?    ")
if pais == "Portichuelo" or pais == "Mapa" or pais == "San Juan":
    print("\nUsted conoce la verdadera escena mapera.")
else:
    print("\nSu padre es dueño del Españolo.")
print("  ")



print("Ejemplo con operador lógico de NOT")
#Con el operador NOT, yo puedo hacer que no se cumpla algo 
print("  ")
#SI PAIS ES NO IGUAL A MAPA/PORTICHUELO/SAN JUAN, se cumple IF NOT
sitio = input("¿Quillo tu de donde eres?    ")
if not sitio == "Portichuelo" or sitio == "Mapa" or sitio == "San Juan":
    print("\nUsted no conoce la verdadera escena mapera.")
else:
    print("\nSu padre es dueño del LEBIS.")


print("OPERADOR DE COMPARACIÓN DIFERENTE --> !")
#Estamos viendo si sitio es diferente a: Portichuelo, Mapa, San Juan 
sitio = input("¿Quillo tu de donde eres?    ")
if  sitio != "Portichuelo" and sitio != "Mapa" and sitio != "San Juan":
    print("\nUsted no conoce la verdadera escena mapera.")
else:
    print("\nSu padre es dueño del LEBIS.")