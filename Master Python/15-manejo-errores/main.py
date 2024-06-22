# Capturar excepciones y manejar errores en código
# susceptible a fallos/errores
# Si se generan errores podemos meterlos en un TRY y EXCEPT, tambien se puede añadir ELSE
# Intruccion final --> FINALLY, detectar cuando termina la intruccion completa
try: 
    nombre = input("¿Cuál es tu nombre: ")

    if len(nombre) > 1: 
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, mete bien el nombre")
else: 
    print("Todo funcionó mi rey")
finally:
    print("Fin de la iteracion")

#Si introduzco un input vacio me aparece NameError 
