"""
Es una lista que dentro tiene otras listas,
por lo que son listas multidimensionales
"""

print("\tLISTA MULTIDIMENSIONAL")

lista = [
    [
        "Antonio",
        "emaildeantonio"

    ],
    [
        "Cañete",
        "emailcelcañete"
    ],
    [
        "pailla",
        "emaildelpailla"
    ],
    [
        "manueljesusgitano",
        "antequeralosabe"
    ]

]
"""
dentro de la lista en lugar de incluir elementos,
incluyo listas.

Hay que tener cuidado como se insertan las listas dentro de la lista
a través de tabulaciones y comas
""" 

"""
para acceder a los elementos de las listas lo especificamos con []
indicando en la posicion dentro de la que esta y si quiero sacar 
un solo elemento de esa lista en especifico lo indico con otro [] indicando
la posicion.

"""

print(lista[1][0])
print("")

#para recorrer la lista entera usamos for con una variable
for informacion in lista:
    for dato in informacion:
        if informacion.index(dato) == 0:
            print("El nombre es " + dato)
        else:
            print("El correo es " + dato)  
    print("\n")
#recorremos ambos datos de las sublistas [0] y [1] usando un for dentro de otro for. El primer for para la propia lista y
#y el segundo para la variable del for anterior