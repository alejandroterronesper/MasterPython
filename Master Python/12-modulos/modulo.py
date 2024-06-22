def holaMundo(nombre):
    return f"Hola {nombre}"

def calculadora(numero1,numero2,basicas =False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    producto = numero1 * numero2
    division = numero1 / numero2

    cadena =""
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