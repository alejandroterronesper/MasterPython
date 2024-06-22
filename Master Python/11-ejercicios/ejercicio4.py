"""
Crear un script que tenga 4 variables: 
-una lista
-un string
-un entero
-un booleano 


Imprimir el mensaje segun el tipo de dato de cara variable

Se recomienda usar funciones para que compruebe estas variables
"""

"""
1- Se definen los tipos de variables
2- se crea una FUNCION con dos PARAMETROS: dato y el TIPO DE DATO
3- dentro de la FUNCION  se crea una VARIABLE ISISATANCE para comprobar el TIPEADO
4-Con un IF comprobamos que los PARAMETROS que vayamos a meter se cumplen. 
"""




lista = ["patata", "arroz"]
cadena = "esto es un string"
numero = 465
booleado = True




print("\n\tCOMPROBAR TIPEADO")
def comprobar(dato, tipo):
    test = isinstance(dato,tipo)
    if test:
        print(f"El dato '{dato}' es tipo {tipo}")
    else:
        print(f"No es un dato {tipo}, es de tipo {type(dato)}") 

comprobar(lista, int)
comprobar(cadena,str)
comprobar(numero,int)
comprobar(booleado,bool)






