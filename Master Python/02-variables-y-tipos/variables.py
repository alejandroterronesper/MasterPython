"""

Una variable es un contenedor de información
que dentro guardará un dato, se pueden crear
muchas variables y que cada una tenga un dato distinto. 
""" 
"""
texto = "Señor Cañete"
texto2 = "Miau"
numero = 2022
decimal = 8.9

#Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("-------------------------------------")

numero = 56
#sustituir valor de las variables 
print(numero)

"""

print("-------------------------------------")


#Concatenación = unir dos variables o strings 
#crear variables y asignarles un valor 
nombre = "Alejandro"
apellido = "Terror"
oficio = "Sepulturero"
print( nombre + "   " + apellido  + "     "  + oficio)

#pasar datos a la funcion print para que concatene es igual que lo de sumar  las variables
print(nombre, apellido, oficio)

#f {} 
print(f"Hola soy {nombre} mi apellido es {apellido} y trabajo como {oficio}.") 

# .format()
print("Hola soy {} de apellido {} y trabajo como {}".format(nombre, apellido, oficio)) 