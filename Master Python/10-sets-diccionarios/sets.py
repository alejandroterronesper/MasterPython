"""
Es una coleccion de dato sin indice ni orden. 
Se definen como una variable con {} --> set = {dato1,dato2...}
"""


colores = {"Azul", "rojo", "amarillo", "rosa"}
sentidos = {
    "tacto",
    "olfato",
    "gusto"
}

print(sentidos)
print(colores)

colores.add("negro")
colores.remove("rojo")


print(type(colores))

print(colores)

