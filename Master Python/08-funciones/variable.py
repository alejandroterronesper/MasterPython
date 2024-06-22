"""
-Variable LOCAL: es la que se DEFINE dentro de la FUNCION
por lo que no se va a poder utilizar fuera de esta
a no ser que hagamos RETURN

-Variable GLOBAL: se definen fuera de la FUNCION y estan 
disponibles tanto fuera como entro de la funcion 

"""

print("\n VARIABLE GLOBAL")

frase = "Tonto el que lo lea"
#VARIABLE GLOBAL

print(frase)

def funcion():
    #frase = "Señoras, señores en el culo tengo flores"
    #VARIABLE LOCAL
    print("Dentro de la funcion")
    print(frase)
    #Ahora el print accede a la variable GLOBAL
    
    year = 2022
    print("DENTRO")
    print(year)


    #para hacer una variable local se convierta a en una global
    #se hace indicando: global variable

    global melodia
    melodia = "Me pillaste Burt Lancaster"
    print("Dentro,  " + melodia)



    return "DATO DEVUELTO" + " " +  str(year)


print(funcion())
print("FUERA,", melodia)
#para acceder a la funcion local fuera de la FUNCION tendria que 
#hacer un return y accedo desde la funcion imprimiendola