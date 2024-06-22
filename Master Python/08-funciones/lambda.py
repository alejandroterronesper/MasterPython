print("\n FUNCIONES LAMBDA")

"""
Es una FUNCION ANONIMA, no necesita nombre, ni parametros
no necesitan def 
son sencillas y ocupan 1 LINEA de codigo
sirven para tareas SIMPLES y REPETITIVAS

se crean a partir de una variable y se usa la funcion lamdba acompañado del parametro
que hay que definirlo para que nos lo devuelva la fun LAMBDA
"""

dime_year = lambda year: f"El año es: {year}"
"""
VARIABLE --> dime_year 
funcion LAMDBA
PARAMETRO --> YEAR
lo que DEVUELVE es -->f"El año es: {year}"
Para llamarla imprimo la VARIABLE y añado el valor del PARAMETRO


"""
print(dime_year(2022))


