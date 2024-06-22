print("\nVamos a aprender a usar el ELIF")
dia = int(input("Introduce el día de la semana:  "))
if dia == 1:
    print("Es lunes")
else: 
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es finde.")

#Cuidar las tabulaciones de if y else
#Es un código muy sucio si tengo que hacer muchas comprobaciones
print('ELIF = "Else if" Si no se cumple la primero condición, pasa a comprobarse la siguiente')
print(" ")

probando = int(input("Dime que día es.  "))
if probando == 1:
    print("Lunes a trabaja")
elif probando == 2:
    print("Martes, poquito a poco.")
elif probando == 3:
    print("Que no se acaba la semana, todavía estamos a miercoles")
elif probando == 4:
    print("Jueves ya no queda na.")
elif probando == 5:
    print("Cuchame que ya es viernes")
else: 
    print("Es finde tío.")