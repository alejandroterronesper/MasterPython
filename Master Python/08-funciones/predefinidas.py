print("\tFUNCION IMPRIMIR = PRINT ")

nombre = "Señor Terror"
print(nombre)


print("\n\tFUNCION TYPE")
#nos da el tipo de dato que tiene la variable
print(type(nombre))


print("\n\tFORMAS DE DETECTAR EL TIPADO DE UNA VARIABLE")
#se hace con la funcion: isistance(VARIABLE, TYPE)
comprobar = isinstance(nombre, bool)

if comprobar: 
    print("Es una STRING")
else:
    print("No es una cadena")

if not isinstance(nombre, bool):
    print("Es una cadena")
else:
    print("Es un float")


print("\n\tLIMPIAR ESPACIOS DE UNA VARIABLE CON UNA FUNCION")
#Se hace con la funcion: variable.strip()
frase ="            acoplado  en la esquASADSAa           "
print(frase)
print(frase.strip())

print("\n\tELIMINAR VARIABLES")
#Se hace con la funcion: del VARIABLE
dato = 1
print(dato)
#del dato
print(dato)

print("\n\tCOMPROBAR VARIABLES VACIAS")
#COn la funcion: len(variable)
if len(frase) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene" + " " + str(len(frase)) + " " + "carácteres.")

print("\n\tENCONTRAR CARACTERES")
#Se usa la funcion: variable.find("caracter")
print(frase.find("acoplado"))

print("\n\tREEMPLAZAR PALABARAS DE STRING")
#se usa la funcion: variable.replace("ORIGINAL","REEMPLAZO")
nueva_frase = frase.replace("acoplado","cañete")
print(nueva_frase)

print("\n\tPROCESAR MAYUSCULAS Y MINUSCULAS")
#para MAYUS: variable.upper() - para MINUS: variable.lower()
print(frase)
print(frase.lower())
print(frase.upper())