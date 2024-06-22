"""
Mostrar el cuadrado de los primeros numeros naturales con:
- BUCLE FOR
- BUCLE WHILE
"""
print("\tCUADRADO DE LOS PRIMERO 60 NUMEROS CON FOR")

"""
primero hay que crear el bucle for con rango de 1 a 61
luego hacer el cuadrado = numero * numero. 
"""

numero = 1

for numero in range (1,61):
    numero = numero * numero
    print(numero)


print("\tCUADRADO DE LOS PRIMERO 60 NUMEROS CON WHILE")

numero = int(1)

while numero <= 60:
    print(f"El cuadrado de {numero} es {numero} x {numero}: {numero * numero}")
    numero += 1

