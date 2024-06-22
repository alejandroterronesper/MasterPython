print("\n INDICES DE LAS LISTAS/ARRAYS")

junji = ["Tomie" , "Uzumaki", "Gyo" ,"Soichi", "Black Paradox"]
satoshi = ["Perfect Blue", "Millennium Actress", "Paranoia Agent", "Tokyo Godfathers", "Paprika"]
notas = ["do", "re", "mi", "fa", "sol", "la", "si"]

"""
- Para sacar la uno de los elementos de la lista, hay que indicar [] en que posicion se encuentra
teniendo en cuenta que las listas empiezan desde 0 -->
lista = [elemento0,elemento1...]

- Tambien se pueden usar numeros negativos, entonces la lista empieza a contar desde el final, 
si son 3, entonces va a ser -1.

-Para sacar varios elementos usamos [elemento1:elemento4] usamos : no la coma (,) por que lo interpreta como un numero decimal.

""" 
print(junji[1])
print(junji[1:3])
print(notas[-5])
print(satoshi[0:])


print("\nSUSTITUYENDO ELEMENTOS DE LA LISTA")

"""
Para ello se indica a a traves de la variable la posicion y por lo que va  a ser sustituido:

variable[elemento1] = "dato que lo sustituye"


"""

junji[1] = "cañete"
print(junji)
print(junji[1])



print("\nAÑADIR ELEMENTOS A UNA LISTA")
"""
hay que usar el elemento  --> lista.append(nuevoelemento)


"""

junji.append("El umbral de lo siniestro")
junji.append("Diatio gatuno")

print(junji)


junji[4] = "damari"
print(junji)

print(junji[4])



