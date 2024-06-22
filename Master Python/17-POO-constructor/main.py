# importar modulo

from coche import Coche
 
carro = Coche("Amarillo", "Renault","Clio")
carro2 = Coche("Rojo", "Seat","Miau")
carro3 = Coche("Azul", "Ibiza","Cleo")
carro4 = Coche("Fosforito", "Leon","Hee hee")



print(carro.getInfo())  
print(carro2.getInfo())  
print(carro3.getInfo())  
print(carro4.getInfo())  


#Detectar tipado
carro4 = "Demoler"
if type(carro4) == Coche:
    print("Usted tiene un", type(carro4))
else:
    print("Mirrey vaya usted a la cafeteria")


# Visibilidad

print(carro.publico)

#print(carro._privado_rey)

print(carro.getPrivado())