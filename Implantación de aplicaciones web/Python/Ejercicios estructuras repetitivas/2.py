#un usuario al entrar dice el dinero que tiene
#Apuesta una cantidad de ese dinero en cada partida y tiene diez oportunidades para adivinar un numero aleatorio, 
#No puede apostar mas del dinero que le queda
#con mensaje diciendo si es mayor o no
#si lo advina gana lo apostado si falla pierde lo apostado
#con la posiblidad de volver a jugar otra vez si le queda dinero
from random import randint

print("Bienvenido al juego de adivinar el numero misterioso.")
dineroDisponible=int(input("Cuanto dinero tiene? "))
#volveraJugar=input("Quiere apostar? ") 
#Iba a utilizar esto para llamar a la variable inicialmente,
#pero creo que tiene mas sentido que por defecto valga "si". Al menos la primera vez.
volveraJugar="si" 

while dineroDisponible>0:
    #Declaramos el fin del programa en caso de que no quiera jugar.
    if volveraJugar.lower()!="si":
        print("Gracias por jugar. Recoga sus ganancias.")
        break
    else:
        dineroApostado=int(input("¿Cuanto dinero quiere apostar? "))
        while dineroApostado>dineroDisponible:
            dineroApostado=int(input("Ingrese una cantidad valida. "))
        
        numeroAleatorio=randint(0,100)
        print("Dispone de un máximo de 10 intentos.")
        intento=int(input("Adivine el numero entre 0 y 100.\n"))
        numeroDeIntentos=0
        while intento!=numeroAleatorio:
            #Declaramos el numero máximo de intentos y en caso de qeu se superen, se salga del bucle.
            if numeroDeIntentos==10:
                print("Se te acabaron los intentos machote.")
                break
            else:
                numeroDeIntentos+=1
                if intento>numeroAleatorio:
                    print("El numero es menor. (Intento "+str(numeroDeIntentos)+")")
                elif intento<numeroAleatorio:
                    print("El numero es mayor. (Intento "+str(numeroDeIntentos)+")")
                intento=int(input())
        if intento==numeroAleatorio:
            dineroDisponible+=dineroApostado
            print("CORRECTO!. Recoja sus ganancias.")
        else:
            dineroDisponible-=dineroApostado
    print("Dispone de "+str(dineroDisponible)+"€")
    volveraJugar=input("¿Quiere volver a apostar? ")

print("No tiene mas dinero para apostar")