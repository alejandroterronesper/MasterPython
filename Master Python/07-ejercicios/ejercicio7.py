#Mostrar numeros impares entre dos numeros 

numero1 = int(input("Dime un numero: "))
numero2 = int(input("Dime otro numero: "))


contador = 1 
numero1 += 1

for contador in range (numero1,numero2):
    if contador % 2 != 0:
        print(f"Los números impares entre el {numero1} y el {numero2} son: {contador}")








