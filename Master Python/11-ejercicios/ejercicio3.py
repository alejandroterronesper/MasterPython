"""
Comprobar si una variable esta vacia
y si esta vacia rellenarla con texto en minusculas y mostrarlo en mayusculas

"""

variable = ""


if len(variable) <= 0:
    print(f"La variable está vacia: {variable}")
    nueva = variable.replace("","el ejercicio está resuelto")
    print(nueva.upper())

#RELLENAR VARIABLE 


