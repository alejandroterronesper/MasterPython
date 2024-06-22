# Programacion orientada a objetos (POO)

"""
Una clase es un molde para crear un objeto 
con características parecidas que son variables
y tienen acciones o funciones


- Clase: molde para crear mas objetos de ese tipo
(Piano) con característica similares, 
usamos class que contiene propiedades, atributos y metodos

-Atributos: caracteristicas del objeto

-Metodo:acciones del objeto
"""
print("MARCA DE PIANO 1")
class Piano:

    #Atributos/propiedades: diferentes características del objeto
    marca = "Yamaha"
    color = "negro"
    teclas = "contrapesadas"
    tempo = 65
    tipo = "electrico"
    teclas = 88


    #Metodos
    def setColor(self,color):
        self.color = color
    
    def getColor(self,color):
        return self.color

    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self,marca):
        return self.marca

    def rapido(self):
        self.tempo += 1
    
    def lento(self):
        self.tempo -= 1
    
    def getTempo(self):
        return self.tempo 
#fin definicion clase


#crear objeto / instanciar clase

piano = Piano()

piano.setColor("Rojo")
piano.setMarca("Thommand")
piano.rapido()
piano.rapido()


print("Tempo nuevo", piano.getTempo(), piano.marca,piano.color)


print("MARCA DE PIANO 2")
#  Crear más objetos

#tenemos acesso a las mismas variables
piano2 = Piano()

print(piano2.color)

piano2.setColor("Azul")
piano2.setMarca("Nintendo")

piano2.lento()

print(piano2.color, piano2.marca)
print(piano2.tempo)
print(type(piano2))