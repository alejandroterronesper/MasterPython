"""
TODAS LAS TABLAS DE MULTIPLICAR
DEL 1 AL 10
-poner título de la tabla de multiplicar
-Multiplicaciones

"""

print("TABLA DE MULTIPLICAR \nDEL 1 AL 10 CON FOR:  ")


"""
#PRIMERO HACER TABLA DE NUMERO CUALQUIERA


numero = 7
for contador in range (1,11):
    print(contador * numero)


# mostrar numeros de la tabla que voy a multiplicar del 1 al 10:

for contador in range (1,11):
    print(contador)

"""

for producto in range (1,11):
    for contador in range (1,11):
        print(f"\n\tLa tabla del {producto} es  {producto} x {contador}: {producto * contador} ")
