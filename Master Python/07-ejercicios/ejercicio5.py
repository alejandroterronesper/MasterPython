"""
Mostrar los números entre los dos números que diga un usuario
"""

print("\tBucle FOR números entre dos números:")
numero1 = int(input("\nIntroduce un número:   "))
numero2 = int(input("\nAhora introduce otro:  "))

contador = 1
numero1 += 1 



for contador in range(numero1, numero2):
    print(contador)
else:
    print(f"Estos son los números del {numero1 - 1} al {numero2}.")





"""
print("\tBucle WHILE números entre dos números:")
numero1 = int(input("\nIntroduce un número:   "))
numero2 = int(input("\nAhora introduce otro:  "))

contador = numero1 + 1

while contador > numero1 and contador < numero2: 
    print(contador)
    contador += 1
else:
    print(f"Estos son los números del {numero1} al {numero2}.")
""" 
