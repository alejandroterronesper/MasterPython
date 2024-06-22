"""
Un condicional es una estructura de control
que me permite controlar el flujo del programa, 
si un dato cumple la condición, se ejecuta
si no la cumple, no se ejecuta
Depende de la entrada de datos
"""

"""
CONDICIONAL IF

if condition:
    Ejecuta grupo de instrucciones
else:
    Se ejecutan otras instrucciones

"""

# EJEMPLO 1
print("             EJEMPLO 1")

color = "ROJITO"

if color == "ROJITO":
    print("El color es ROJITO e.e")
else:
    print("No es rojito mi rey")


# EJEMPLO 2

print("             EJEMPLO 2")

color = "ROJITO"

if color == "NEGRO":
    print("El color es ROJITO e.e")
else:
    print("No es rojito mi rey")

# EJEMPLO 3 

print("             EJEMPLO 3")

color = input("¿Adivine de que color es el videito mi rei e.e ")

if color == "ROJITO":
    print("El color es ROJITO e.e")
else:
    print("No es rojito mi rey")
