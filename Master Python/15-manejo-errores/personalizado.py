# Excepciones personalizadas o lanzar error
# para invocar un error usamos raise ValueError 



try:
    nombre = input("Dime tu nombre:     ")
    edad = int(input("Dime tu edad:      "))

    if edad < 5 or edad > 110:
        raise ValueError("Introduce una edad real")
    elif len(nombre) <= 1:
        raise ValueError ("Introduce un nombre correcto")
    else:
        print(f"Bienvenido {nombre}")
except ValueError:
    print("Introduce correctamente los datos")