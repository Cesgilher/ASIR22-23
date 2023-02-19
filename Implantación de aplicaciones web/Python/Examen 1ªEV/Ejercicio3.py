#Declaramos las variables y las pedimos por terminal
golesMessi=int(input("CUantos goles ha marcado Messi? "))
porcentajeParadasUnai=float(input("Cual es el porcentaje de paradas de Unai Simon(entre 0 y 1)? "))
posesionMediaEspaña=float(input("Cual es la media de posesion de España(entre 0 y 1)? "))
tarjetasRojasaBrasil=int(input("Cuantas targetas rojas ha recibido Brasil? "))
golesMbape=int(input("Cuantos goles ha marcado Mbape? "))
primaDeArabiaSaudi=int(input("Cuanto cobran los jugadores de Arabia Saudi por marcar un gol? "))

#Declaramos cada condicion.

if golesMessi>8:
    ganador="Argentina"
elif golesMessi>4 and golesMessi<8:
    if porcentajeParadasUnai>0.9 and tarjetasRojasaBrasil>1:
        ganador="Alemania"
    elif posesionMediaEspaña>0.75 and golesMbape<3:
        ganador="España"
    elif tarjetasRojasaBrasil==0 and golesMbape>5:
        ganador="Francia"
    elif golesMbape>5 or posesionMediaEspaña<0.6:
        ganador="Brasil"
elif primaDeArabiaSaudi>=1000000000000:
    ganador="Arabia Saudí"
elif tarjetasRojasaBrasil>3 and golesMbape<3 and posesionMediaEspaña<0.5 and porcentajeParadasUnai<0.5:
    ganador="Japon"
else:
    ganador="¡desconocido!"





print("El ganador del mundial será",ganador)

