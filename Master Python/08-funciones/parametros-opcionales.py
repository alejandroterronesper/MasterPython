"""
Los parametros opcionales: Podemos PASARLE o NO ese DATO

Para ello, hay que darle un valor al parametro
que queramos que sea opcional parametro2 = "Opcional"
Si no queremos que se muestre el parametro cuando no llega 
el dato deseado, hacemos un if 
"""

def empleado(nombre,ID = None):
    print("EMPLEADO")
    print(f"El nombre es {nombre}")
    if ID != None:
        print(f"Su DNI es {ID}")



empleado("Antonio", "4546656a")