print("\tNUMEROS PARES DEL 1 AL 120")

"""
Tengo que tener en cuenta dos cosas:
    - CREAR UNA CONDICIONAL QUE ME MUESTRE NUMEROS PARES --> numero % 2 = 0
    - MOSTRAR NUMEROS DEL 1 AL 100. 
""" 

print("\nHECHO CON BUCLE FOR")
numero = 1 

for numero in range (0,121):
    if numero % 2 == 0:
        print(numero)
else:
    print("\tTODOS LOS NUMEROS PARES DEL 1 AL 120")



print("\nHECHO CON BUCLE WHILE")
numero = 1 

while numero <=120:
    numero += 1
    if numero % 2 == 0:
        print(numero) 
else:
    print("\tTODOS LOS NUMEROS PARES DEL 1 AL 120")


