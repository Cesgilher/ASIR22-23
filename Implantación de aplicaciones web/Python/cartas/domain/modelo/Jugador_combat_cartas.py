class Jugador:

    def __init__(self, nombre :str,apellidos:str ,puntos:int =0, carta=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.puntos = puntos
        self.carta = carta
        

    def nombre_completo(self):  
        return self.nombre + " " + self.apellidos

    def __str__(self):
        return self.nombre + " " + self.apellidos + " " + str(self.puntos)
