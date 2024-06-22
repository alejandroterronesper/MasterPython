"""
Vamos a ver los parametros en las funciones

nombre = "Agua"

def mostrarnombre(): 
    print(f"Tu nombre es: {nombre}")

mostrarnombre()
mostrarnombre()


Queremos que el nombre se dinamico,
cada vez que se llame a las funciones 
tenga un nombre distinto 

Para ello hay que pasarle un parametro --> nombre() <--- hay que definirlo: () --> (parametrodefinido)


"""

#EJEMPLO 1

print("\t\tEJEMPLO 1")

def nombre(algo):
    print(f"Esto es: {algo}")

nombre("Agua")
nombre("Cacahuete")
nombre("Lechuga")

# IMPRIMIRE EL NOMBRE QUE PASAMOS POR PARAMETRO, POR EL PARAMETRO PASAMOS DIFERENTES DATOS
#creamos una variable en ese parametro es decir nombre = "VALOR DEL PARAMETRO"

#tambien podemos pasarlo como PARAMETRO

respuesta = input("Dime tu nombre:  ")
edad = int(input("Dime tu edad: "))

def ejemplo(respuesta,edad):
    print(f"Tu te llamas: {respuesta}")

    if edad >= 18:
        print(f"El usuario {respuesta} es mayor de edad.")

ejemplo(respuesta,edad)

"""
Parametro es un dato que le paso desde fuera a dentro de la funcion
y asi puedo parametrizar la funcion
"""

#EJEMPLO 2

print("\n\t\tEJEMPLO 2")


print(" Tabla de multiplicar usando funciones")




def calcular(numero):
    for tabla in range (11):
        producto = numero * tabla
        print(f" La tabla de {numero} es {numero} x {tabla}: {producto}")


    print("\n")




calcular(3)
calcular(5)


print("\n\tAhora todas las tablas de multiplicar")

for tablon in range (1,11):
    calcular(tablon)

"""
tablon que usa el bucle for, funciona como si pusieramos una y otra vez:
calcular(1),calcular(2) etc
Aqui tablon esta en un bucle y va a ir pasando por los numeros del rango
"""