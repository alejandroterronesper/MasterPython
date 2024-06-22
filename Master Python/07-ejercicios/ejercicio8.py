# Calcular el X % de un número al azar  

"""
crear dos variables de entrada, 
una que nos pida el numero
y otra el tanto por ciento que queremos aplicar
luego hacer una variable con la operacion. 

(numero x porcentaje)/100 
"""

numero = int(input("Dime un número: "))
porcentaje = int(input("Dime que porcentaje quieres:    "))

calculo =  (numero * porcentaje)/100  

print(f" El {porcentaje}% de {numero} es ({porcentaje} x {numero})/100: {calculo}")