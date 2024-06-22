"""
Bucle WHILE repite tantas veces como sea necesario
en base a una CONDICIÓN. 
Pero hay que CONTROLAR al CONTADOR, la VARIABLE tiene que
aumentar de valor para que la CONDICIÓN termine y se salga del BUCLE. 

Estructura de control que repite la ejecución
de una serie de instrucciones tantas veces como sea necesario
hasta que deje de cumplirse la función. 


while condicion:
    bloque de instrucciones 
    actualización de contador

Es neceseario la presencia de un CONTADOR porque la condición 
siempre se va a evaluar el contador que siempre tiene que ACTUALIZARSE
para que el BUCLE siga avanzando
"""

print("\tEjemplo de contador mostrando numeros del 1 al 100")

contador = 1
while contador <= 100:
    print(f"Los numeros del 1 al 100:  {contador}")
    contador += 1 

"""
hay que actualizar el contadorque aumente en 1,
es decir, por cada vuelta que de tiene que actualizarse porque
sino no termina, entonces siempre estaria poniendo 1,
porque el CONTADOR no se actualiza, por cada vuelta que da,
se actualiza, se le suma 1:
--> 1, contador + 1= 2
-- > 2, contador +1 = 3 etc 
"""

print("    ")

"""
Los vamos a separar por comas:
Para ello hay que crear un STRING que sea 0 
para crear una variable a la que poder añadirle la "," y añadirle el CONTADOR
en formato STRING, y todo esto se une a traves de adiciones es decir
muestrame (0) + " ," + contador (numero del 1 al 100) = MUESTRAME
entonces al imprimir muestrame imprime lo siguiente=
0 , 1 --> muestrame = 1 --> 1, 2 etc.. 
"""


contador = 1
muestrame = str(0)
while contador <= 100: #CONDICION 
    muestrame = muestrame + ", " + str(contador)
    contador += 1 #ACTUALIZADOR DEL CONTADOR 
print(muestrame)


"""
ELEMENTO DEL BUCLE WHILE
-CONTADOR 
-CONDICION
-ACTUALIZADOR del CONTADOR 
"""