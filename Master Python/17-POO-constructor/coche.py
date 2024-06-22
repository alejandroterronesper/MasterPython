class Coche:
    #Atributos y propiedades
    color = "rojo"
    marca  = "ford"
    modelo = "GT 500"
    velocidad = 300
    caballaje = 150
    plazas = 2
    publico = "Soy un colegio publico"
    __privado_rey = "Soy un colegio de pago :("
    
    #Metodo Constructor
    def __init__(self, color, marca, modelo):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        #self.velocidad = velocidad
        #self.caballaje = caballaje
        #self.plazas = plaza
 
    #Metodos Accesores SET Y GET
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
 
    def getPrivado(self):
        return self.__privado_rey

    
    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca
 
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def getModelo(self):
        return self.modelo
    
    def getVelocidad(self, velocidad):
        self.velocidad = velocidad
    
    
    def getCaballaje(self, caballaje):
        self.caballaje = caballaje
    
    def SetCaballaje(self):
        return self.caballaje
    
    def getPlazas(self, plazas):
        self.plazas = plazas
    
    def setPlazas(self):
        return self.plazas
    
 
    def getInfo(self):
        info = "---- Informacion del Coche---"
        info += "\n Color: "+ self.getColor()
        info += "\n Marca: "+ self.getMarca()
        info += "\n Modelo: "+ self.getModelo()
        #info += "\n Velocidad "+ str(self.getVelocidad())
 
        return info