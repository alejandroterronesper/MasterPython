#metodos y funciones de listas

junji = ["Tomie" , "Uzumaki", "Gyo" ,"Soichi", "Black Paradox"]
numeros = [1,7,3,9,5]


print("\tORDENAR UNA LISTA")
#usamos la funcion lista.sort()
print(f"Desordenado {numeros}")

junji.sort()
print(f"Ordenados {junji}")
#ordena los numeros y las palabras, alfabeticamente


print("")
print("\tAÑADIR ELEMENTOS A LISTA")
#usamos la funcion .append()

junji.append("cañete")
print(junji[5])

#otra manera es con .insert(POSICION, "Nuevo dato")
junji.insert(3,"cañete")
print(junji)
print("")

print("\tELIMINAR ELEMENTOS DE LA LISTA")
#usamos la funcion .pop(), dentro ponemos el valor que tiene, uno numerico
junji.pop(0)
print(junji)

#si queremos hacerlo por el nombre usamos lista.remove("Elemento eliminar")
junji.remove("cañete")
print(junji)
print("")


print("\tDAR LA VUELTA A LA LISTA")
#usamos la funcion .reverse()

numeros.reverse()
junji.reverse()

print(numeros + junji)

print("")

print("\tBUSCAR ELEMENTO EN LA LISTA")
# se hace en un print indicando el elemento IN lista
print("Tomie" in junji)
# el resultado por pantalla sera True o False

print("")


print("\tCONTAR NUMERO DE ELEMENTOS")
# usamos la funcion len(lista)
print(len(junji))
print("")

print("\tCUANTAS VECES APARECE UN ELEMENTO")
# usamos el parametro .count("VALOR")

print(junji.count("Tomie"))
print(numeros.count(3))

print("")

print("\tCONSEGUIR INDICE DE UN ELEMENTO DE LA LISTA")
# se hace a través del parametro .index("VALOR")

print(junji.index("Tomie"))
print("")

print("\tUNIR VARIAS LISTAS")
#usamos la funcion .extend --> lista.extend(lista2)

junji.extend(numeros)
print(junji)
