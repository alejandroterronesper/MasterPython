# VAMOS A VER LOS IF ANIDADOS, IF DENTRO DE OTRO IF
print("\tEJEMPLO IF ANIDADO para comprobar la mayoría de edad ")
print("     ")
nombre = "Señor Terror"
ciudad = "Pedanía de Antequera"
contienete = "CHINA"
edad = 18
mayoria_edad = 18

#Usamos los comparadores
if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if contienete != "Europa":
        print("Es un inmigrante.")
    else:
        print(f"Es de los nuestros de {ciudad}")

else:
    print(f"{nombre} no tiene la mayoría de edad.")
