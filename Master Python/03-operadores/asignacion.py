# operadores de asignación
(print(" \t OPERADORES DE ASIGNACIÓN"))
dinero = 6565

# el operador de asignación puede ser tambien += , -=, *=, /=, %=

dinero += 89898

print(dinero)

dinero %=3

print(dinero)

print(type(dinero))

"""
operadores de incremento y decremento 
aumentan o disminuyen el valor de su operando en 1
en python no puede expresarse como:

numero++ 
numero--
--numero
++numero

para ello tenemos que usar los operadores de asignación y aritmeticos
""" 

numero = 89

print("\t INCREMENTO")
numero += 1
numero = numero + 1
print(numero)

print("\t DECREMENTO")
numero -= 1
numero = numero - 1 
print(numero)

#pre incremento 
print("\t PRE INCREMENTO")

numero = 1 + numero
print(numero)


#pre decremento 

print("\t PRE DECREMENTO")
numero = 1 - numero

print(numero)
