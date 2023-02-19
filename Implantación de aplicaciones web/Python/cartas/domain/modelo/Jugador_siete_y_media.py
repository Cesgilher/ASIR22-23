from domain.modelo.Carta import Carta

class Jugador:

    def __init__(self, nombre :str,apellidos:str ,carta:Carta=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.carta = carta
        self.suma_cartas = 0
        
        

    def nombre_completo(self):  
        return self.nombre + " " + self.apellidos

    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + str(self.puntos)