#Parametros opcionales y return/devolver datos



"""
definir una funcion y se le pasa un parametro
dentro de la funcion se imprimir con print la string
pero dentro de la funcion se puede hacer una VARIABLE e imprimir el PARAMETRO

el RETURN nos permite DEVOLVER UN DATO que esta dentro de la funcion a fuera 
cuando se le invoque 

"""

# Hay que poner la VARIABLE dentro de la FUNCION

def propicio(nombre):
    saludo = f"Propicios días {nombre}" 

    return saludo

#el RETURN te devuelve la VARIABLE que hay dentro de la FUNCION

print(propicio("Caballero"))


print("\n     CALCULADORA")



def calculadora(numero1,numero2, basicas= False):
    #variables con los parametros
    suma = numero1 + numero2
    resta = numero1 - numero2
    producto = numero1 * numero2
    division = numero1 / numero2

    cadena =""
    #con condicionales se crea el parametro opcional
    if basicas != False:
        cadena += "suma: " + str(suma)
        cadena += "\n"
        cadena += "resta:  " + str(resta)
        cadena += "\n"
    else:
        cadena += "producto:  " + str(producto)
        cadena += "\n"
        cadena += "division:  " + str(division)

    return cadena


#Se le asignan variables a la cadena
#Se crea la condicion que depende del parametro secundario "Basicas"
print(calculadora(5, 8, True))