print("\nRECORRER LISTAS")

"""
Parar recorrer una lista, podemos hacerlo mediante
el bucle FOR. 

for variable_donde_se_guardan in lista 

asi que por cada vuelta que de el bucle en la LISTA, 
va a ir guardandolo en la VARIABLE
"""

junji = ["Tomie" , "Uzumaki", "Gyo" ,"Soichi", "Black Paradox"]


for manga in junji:
    print(manga)


"""
Se puede sacar el nº del indice de cada elemento de la lista 
a través de la funcion lista.index(variable), con esto saca el número.
"""
print("")

for manga in junji: 
    print(f"{junji.index(manga) + 1}. {manga}")


print("\nAGREGAR ELEMENTOS A LA LISTA CON INPUT")

nuevo_manga = " "
#hay que definir previamente el input como " "
#asi creamos un bucle infinito que guarde elementos
    #en la lista
while nuevo_manga != "parar":
    nuevo_manga = input("Introduce un manga:    ")


    if nuevo_manga != "parar": 
        junji.append(nuevo_manga)
    #para que no aparezca en el apendice de la lista el dato parar, hay que indicarse al append con un IF

#para añadir estas entradas a la lista, usamos la funcion .append()
#lista.append(variable_input)
#para que loes nuevos elementos se vean por pantalla en la lista, hay que crear un bucle FOR, con OTRA VARIANTE
for manga in junji: 
    print(f"{junji.index(manga) + 1}. {manga}")


#para añadir dato a lista se usa APPEND y para listar los elementos usamos INDEX

