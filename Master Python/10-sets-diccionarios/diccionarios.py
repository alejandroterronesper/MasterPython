"""
Es parecido a una lista, en lugar de tener indices NUMEROS, tiene INDICES ALFANUMERICOS
almacena datos, en formato clave --> valor
parecido a un array asociativo o un objeto json. 

ej.

diccionario = {
    "clave": "valor"
}
"""

print("DICCIONARIO EJEMPLO")
print("")
persona = {
    "nombre": "Alejandro",
    "apellidos": "Terrones",
    "oficio": "gotico"
}


print(persona)
print(type(persona))

#podemos acceder a los diferentes indices del diccionario 
#print(diccionario["clave1"]) --> valor1

print(persona["nombre"])


print("")
print("DICCIONARIOS DENTRO DE LISTAS")
# Una lista que contiene diccionarios --> [{}]
#es combinar una lista con los diccionarios
#posee un indice alfanumerico
#SEPARAR las claves con COMA!
personas = [
    {
        "autor": "Junji Ito",
        "manga": "Tomie"
    },
    {
        "autor": "Satoshi Kon",
        "manga": "Opus"

    },
    {
        "autor": "Inio Asano",
        "manga": "Oyasumi PunPun"
    }
]


# para buscar utilizo el INDICE de la LISTA -numero- y en el DICCIONARIO el INDICE ALFANUMERICO
print(personas[1]["manga"])

personas[1]["autor"]= "cañete"
print(personas)

for persona in personas:
    print(f"El autor es: {persona['autor']}")
    #FIJARSE BIEN EN LA ESTRUCTURA DE COMILLADO 1º "DOBLE COMILLA", DENTRO 'COMILLA'
    print(f"El manga es: {persona['manga']}")
    print("")



