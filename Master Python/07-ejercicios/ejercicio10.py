"""
Programa para pedir la nota de 15 alumnos 
y  sacar cuantos han aprobado en numero y cuantos han suspendido en numero. 


dar la nota de cada uno
y mostrar en pantalla
han aprobado x - han suspendido y
"""

"""
alumno = input("Dime nombre del alumno: ")
nota = int(input("Dime su califiación:  "))

if nota >= 5:
    print(f"{alumno} está aprobado.")
else:
    print(f"{alumno} ha suspendido")

SUSPENSO
"""


"""
Se puede hacer con While o con For
Vamos a ejecutar el bucle tantas veces 
como se nos indique, en este caso 15. 
"""
"""
contador = 0
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuántos alumnos tienes?        "))

con esta variable se define a numero_alumnos
para que en el bucle while el contador tenga un limite
el contador por cada vuelta va a sumar 1 hasta llegar a 15
con las condicionales se crea la condicion nota <= 5 
al cumplirse se le suma 1 a aprobado
si no, se le suma 1 a suspendos 



while contador <= numero_alumnos:
    nota = int(input(f"¿Qué nota quieres ponerle a \"alumno{contador}\" "))
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1
    contador += 1

print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspensos: {suspendidos}")

""" 

aprobados = 0
suspensos = 0

alumnos = int(input("Numero de alumnos: "))
contador = 0 

for contador in range (contador, alumnos): 
    nota = int(input("Dime la nota: "))
    if nota >= 5:
        aprobados = aprobados + 1
    else:
        suspensos = suspensos + 1

print(aprobados)
print(suspensos)

