"""
Operadores de comparación 
 
==      --> IGUAL 
!=      --> DIFERENTE
<       --> MENOR
>       --> MAYOR
<=      --> MENOR QUE
>=      --> MAYOR QUE

Operadores lógicos

and --> y
not --> no
or  --> or
!   --> negación
"""
print("\tEJERCICO 1")
year = 2020


if year >= 2021:
    print("Estamos en el año 2021 pa lante.")
else:
    print("Es un año anterior a 2021.") 

print("\nEJERCICO 2")

"""
IMPORTANTE que todo lo que pasa por INPUT se transforma en un dato STRING
nosotros queremos pasar un NUMERO, por lo que tenemos que pasarlo a INT 
"""
year = int(input("¿Qué año es?  "))


if year < 2021:
    print("\nEstamos en el año 2021 pa lante.")
else:
    print("Es un año anterior a 2021.")