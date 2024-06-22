print("Tabla de multiplicar")

numero = int(input("Dime el número: "))

if numero < 1:
    numero = 1

print(f"Tabla de multiplicar de {numero}")

#DEFINIR CONTADOR

contador = 1


#AQUI SE PONE LA CONDICIÓN PARA QUE NO SEA INFINITO Y PARE 
while contador <=10: 
    print(f" {numero} x {contador} = {numero * contador}")
    contador += 1 
else: 
    print("Tabla terminada. ")