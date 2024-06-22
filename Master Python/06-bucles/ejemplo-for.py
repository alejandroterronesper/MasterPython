#TABLA DE MULTIPLICAR 

numero = int(input("¿De qué numero quieres la tabla?    "))

if numero < 1:
    numero = 1
"""
podriamos poner numero >=1
pero para ahorrarnos un ELSE
colocamos numero <1
y para que se pueda realizar, reasignamos valor
numero = 1 
entonces se cumple la condicion if 

"""
print(f"\tYabla de multiplicar de {numero}")

# Recorremos el rango del 1 al 11 

for tabla in range (1, 11):
    if numero == 85:
        print(f"{numero} este no mi rey.")
        break
    
    #dentro del bucle de pueden incluir condiciones e instrucciones
    # queremos que se corte el bucle a traves de
    # la instruccion BREAK 
    
    print(f"\n{numero} x {tabla} = {numero * tabla}")

  

else: 
    print("\tTabla finalizada.")

