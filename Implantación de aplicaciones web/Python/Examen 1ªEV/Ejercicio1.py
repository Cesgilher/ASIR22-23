from random import randint


jugador1=input("Como te llamas jugador1? ")
jugador2=input("Como te llamas jugador2? ")
puntosJugador1=0
puntosJugador2=0

#Llamamos a la moneda
moneda=randint(0,1)
monedaJugador1=input(jugador1+" elige si cara o cruz: ")
print("Vamos a tirar la moneda")



if monedaJugador1.lower()=="cara":
    monedaJugador1=0
else:
    monedaJugador1=1

if moneda==0:
    print("Ha salido cara")
else:
    print("Ha salido cruz")

if monedaJugador1==moneda:
    jugando=0    
else:
    jugando=1
intentos=0
#Lo pongo asi para que cuando llegue a 6 compruebe quien ha ganado 
while intentos<6:
    dado=randint(1,6)
    #Cuando llegue a 5 intentos o cualquiera de los dos participantes tenga tres puntos, "intentos" pasará a valer 6 y se acabara el bucle
    if puntosJugador1==3:
        print("Enhorabuena",jugador1,"has ganado la partida!")
        intentos=5
    elif puntosJugador2==3:
        print("Enhorabuena",jugador2,"has ganado la partida!")
        intentos=5
    elif jugando==0:
        print("Es tu turno",jugador1)
        eleccionDelJugador1=input("Par o impar? ")
        if (eleccionDelJugador1.lower()=="par" and dado%2==0) or (eleccionDelJugador1.lower()=="impar" and dado%2==1):
            puntosJugador1+=1
            print("Correcto, sumas un punto",jugador1)
        else:
            puntosJugador2+=1
            print("Error, suma un punto",jugador2)
    else:
        print("Es tu turno",jugador2)
        eleccionDelJugador2=input("Par o impar? ")
        if (eleccionDelJugador2.lower()=="par" and dado%2==0) or (eleccionDelJugador2.lower()=="impar" and dado%2==1):
            puntosJugador2+=1
            print("Correcto, sumas un punto",jugador2)
        else:
            puntosJugador1+=1
            print("Error, suma un punto",jugador1)
    intentos+=1
    
    #Vamos variando el valor de jugando entre 0 y 1 cada partida para que cambie quien elige.
    jugando=(jugando+1)%2        
            
    

