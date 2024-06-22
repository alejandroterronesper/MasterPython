from unittest import expectedFailure


try:
    numero = int((input("Dime el cuadro de :      ")))
    print(f"El cuadrado de {numero} es: {numero * numero}") 
except TypeError:
    print("Debes convertir tus STR a INT")
#except ValueError:
#print("Dime un numero")
except Exception as error:
    print("Ha ocurrido el error:", type(error).__name__)

#Se generan error como TypeError: si no pongo INT en la VARIABLE numero 
# O ValueError si en el INPUT doy STR en lugar de INT 