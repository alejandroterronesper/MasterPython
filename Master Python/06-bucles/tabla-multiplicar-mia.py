"""
Crear tabla de multiplicar a partir del número dado
"""

numero = int(input("Dime un número y te diré su tabla de multiplicar:  "))
 

if numero >= 1:
    for tabla in range(0,11):
        print(f"La tabla de multiplicar de {numero} es: {numero} x {tabla} = {tabla * numero}")


