from domain.modelo.Jugador_combat_cartas import Jugador
from domain.modelo.baraja import Baraja
from domain.servicios.servicios_cartas import ServiciosCartas


# ejecucion cosas
def main():
    serviciosCartas = ServiciosCartas()
    baraja : Baraja = serviciosCartas.crear_baraja()

    serviciosCartas.mezclar_baraja(baraja)
    cantidadJugadores = int(input("Introduce la cantidad de jugadores: "))
    jugadores: list[Jugador] = []
    
    #Pedir jugadores
    for i in range (0,cantidadJugadores):
        nombre = input("Introduce el nombre del jugador: ")
        apellido = input("Introduce el apellido del jugador: ")
        jugador: Jugador = Jugador(nombre,apellido)
        jugadores.append(jugador)       
   
        # Combat cartas
        
    
    #lo que ejecuta cada ronda
    for i in range (0,40,cantidadJugadores):
        if i+cantidadJugadores>40:
            break
        else:
            print("Ronda",int(i/cantidadJugadores)+1)
            
            # saca una carta para cada jugador
            for j in range (0,cantidadJugadores):
                print(baraja.cartas[i+j],"para",jugadores[j].nombre)
                jugadores[j].carta=baraja.cartas[i+j]
        
            #comprueba quien tiene la carta mas alta
            cartaMasAlta = jugadores[0]
            empate = False
            for j in range (1,cantidadJugadores):
                if jugadores[j].carta.valor.value > cartaMasAlta.carta.valor.value:
                    cartaMasAlta = jugadores[j]
                    empate = False
                elif jugadores[j].carta.valor.value == cartaMasAlta.carta.valor.value:
                    empate = True
            #un punto al jugador que la tenga mas grande
            if empate == False:
                cartaMasAlta.puntos += 1
                print(cartaMasAlta.nombre,"gana la ronda")
            else:
                print("Empate,nadie puntua")

    #lo que se ejecuta al final de la partida

    print("\npuntos actuales")
    
    for i in range (0,cantidadJugadores):
        print(jugadores[i])

    #comprueba quien tiene mas puntos y por lo tanto es el ganador
    ganador = jugadores[0]
    empate = False
    for i in range (1,cantidadJugadores):
        if jugadores[i].puntos > ganador.puntos:
            ganador = jugadores[i]
            empate = False
        elif jugadores[i].puntos == ganador.puntos:
            empate = True
    if empate == False:
        print(ganador.nombre_completo() ,"gana la partida con",ganador.puntos,"puntos")
        
    else:
        print("Empate, no hay ganador")
    

    

        






#carta = baraja.siguiente_carta()
#while (carta != None):
    #   print(carta)
    #  carta = baraja.siguiente_carta()

    



#for carta in baraja.cartas:
    # print(carta)

