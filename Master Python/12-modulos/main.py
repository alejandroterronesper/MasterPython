"""
Un modulo son funcionalidades ya hechas para reutilizar.

Los modulos de python puden consultarse aqui: 
https://docs.python.org/3/py-modindex.html

Podemos descargar librerias de modulos
o crearlos. 
"""

print("IMPORTAR MODULO")


import modulo

print(modulo.holaMundo("Señor Cañete"))
print(modulo.calculadora(2,3,True))

print("")
print("-------------------------------------------------")
print("")
print("Para traer una sola funcion")

from modulo import holaMundo

print(holaMundo("ñere"))

print("IMPROTAR TODAS LAS FUNCIONES --> IMPORT *")
from modulo import *
print(calculadora(8,8,True))