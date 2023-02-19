from enum import Enum

class Carta:
    class PALOS(Enum):
        OROS = 0
        COPAS = 1
        ESPADAS = 2
        BASTOS = 3
        
    class NUMEROS(Enum):
        AS = 1
        DOS = 2
        TRES = 3
        CUATRO = 4
        CINCO = 5
        SEIS = 6
        SIETE = 7
        SOTA = 8
        CABALLO = 9
        REY = 10  
    def __init__(self, valor : NUMEROS, palo:PALOS):
        self.valor = valor
        self.palo = palo
       
        
    def __str__(self) :
        return  str(self.valor.name) + " de " + str(self.palo.name)


