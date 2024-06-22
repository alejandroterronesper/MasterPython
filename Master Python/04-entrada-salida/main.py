# entrada

nombre = input("¿Cuál es tu nombre? ")
print("\n")
"""
la edad aqui está en formato STR en la salida 
hay que pasarlo a formato INT 
en el caso de que se hagan operaciones aritméticas
"""
edad = input("¿Cuál es tu edad? ")

#todo lo que se recibe por el input se transforma en STR, incluido los numeros 

# salida
print("\n")
print(f"¡Encantado de conocerte {nombre}! \n Veo que tienes {int(edad) + 5}")

