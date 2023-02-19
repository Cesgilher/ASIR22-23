from domain.modelo.Jugador_siete_y_media import Jugador
from domain.modelo.baraja import Baraja
from domain.servicios.servicios_cartas import ServiciosCartas
from domain.modelo.Carta import Carta

def main():
    serviciosCartas = ServiciosCartas()
    baraja : Baraja = serviciosCartas.crear_baraja()
    serviciosCartas.mezclar_baraja(baraja)
    print("Bienvenido al juego de las siete y media. Cada carta vale su valor numerico,\nexcepto las mayores de siete, que valen 0.5.\nEl objetivo es conseguir 7.5 o menos sin pasarse.")
    cantidadJugadores = int(input("Introduce la cantidad de jugadores: "))
    jugadores: list[Jugador] = []
    
    #Pedir jugadores
    for i in range (0,cantidadJugadores):
        nombre = input("Introduce el nombre del jugador: ")
        apellido = input("Introduce el apellido del jugador: ")
        jugador: Jugador = Jugador(nombre,apellido)
        jugadores.append(jugador)

    # repartir cartas

    for i in range (0,cantidadJugadores):
        
        respuesta="si"
        while respuesta=="si":
            carta=baraja.siguiente_carta()
            print(carta,"para",jugadores[i].nombre)
            if carta.valor.value > 7:
                jugadores[i].suma_cartas += 0.5
            else:
                jugadores[i].suma_cartas += carta.valor.value
                
            if jugadores[i].suma_cartas > 7.5:
                print("Te has pasado")
                respuesta="no"
            #en caso de qeu alguno llegue a 7.5 se acaba el juego
            elif jugadores[i].suma_cartas == 7.5:
                print("¡Enhorabuena",jugadores[i].nombre_completo,"has ganado!")
                exit()
            else:
                respuesta = input("¿Quieres otra carta? (si/no)")
        
    # en caso de que ninguno llegue a 7.5 o se haya pasado se compara quien se ha quedado mas cerca
    ganador = jugadores[0]
    for i in range (0,cantidadJugadores):
        if jugadores[i].suma_cartas< 7.5 or jugadores[i].suma_cartas==7.5:
            if jugadores[i].suma_cartas > ganador.suma_cartas:
                ganador = jugadores[i]
                empate=False
            elif jugadores[i].suma_cartas == ganador.suma_cartas:
                empate=True
        else:
            jugadores[i].suma_cartas = 0
    if empate:
        print("Empate")
    else:
        print("El ganador es",ganador.nombre_completo(),"con",ganador.suma_cartas,"puntos")