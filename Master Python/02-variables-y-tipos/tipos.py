#TIPOS DE DATOS

nada = None

# imprimir variable
print(nada)

# mostrar tipo de dato

print(type(nada)) 

#las cadenas = STRINGS (str) pueden incluir frases, son CADENAS DE TEXTO = STR 

cadena = "Hola soy el Señor Terror"
print(cadena)
print(type(cadena))


#Numeros enteros = INT 
entero = 878797979 

print(entero)
print(type(entero))

#Números decimales --> FLOTANTE = FLOAT 
flotante = 78787.7
print(flotante)
print(type(flotante))

#booleanos para ver si es verdadero (True) o falso (False) = BOOL 
booleano = True 
print(booleano)
print(type(booleano))


#lista es una colección de muchas variables, de muchos datos  = LIST
lista = [100, 50, 65]

print(lista)
print(type(lista))

#lista de strings, lista variada de datos = LIST
listastring = ["señor cañete", 50, "depresión"]

print(listastring)
print(type(listastring))

#tupla, lista de datos que no pueden cambiar, es igual que una lista pero se utilizan () = TUPLE
tupla = ("Bienvenidos", "al", "Infierno")
print(tupla)
print(type(tupla))

#diccionarios, te permite tener clave y valor, colección de datos de clave y valor, similar a documento JSON =DICT 
diccionario = {
    "nombre": "Señor",
    "apellido": "Terror",
    "oficio": "satanico"
}

print(diccionario)
print(type(diccionario))

#rango , defino range, secuencia
rango = range(45)

print(rango)
print(type(rango))

#byte, hay que poner la b = BYTES

ola_byte = b"98"
print(ola_byte)
print(type(ola_byte))


"""
Pasar de un dato a otro, por ejemplo si quiero concatenar una str y un int no podría
porque no están en el mismo formato 
""" 
string = "cañete"
numero_entero = 23232
numero_entero = str(23232)

print(f"Hola soy {string}  y me gusta {numero_entero}")

numero_entero = int(23232)

print(type(numero_entero))

numero_entero = float(232323)

print(numero_entero)

print(type(numero_entero))

