from random import randint
print("Bienvenido al juego de adivinar el numero misterioso")
dineroDisponible=int(input("Cuanto dinero tiene: "))
volveraJugar=input("quiere apostar? ")

while dineroDisponible>0:

    if volveraJugar.lower()!="si":
        print("Gracias por jugar. Recoga sus ganancias.")
        exit()
    else:
        dineroApostado=int(input("¿Cuanto dinero quiere apostar? "))
        while dineroApostado>dineroDisponible:
            dineroApostado=int(input("Ingrese una cantidad valida. "))
        
        numeroAleatorio=randint(0,100)
        print("Dispone de un máximo de 10 intentos.")
        intento=int(input("Adivine el numero entre 0 y 100: "))
        numeroDeIntentos=0
        while intento!=numeroAleatorio:
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
            print("CORRECTO!. Recoja sus ganancias ")
        else:
            dineroDisponible-=dineroApostado
    print("Dispone de "+str(dineroDisponible)+"€")
    volveraJugar=input("quiere volver a apostar? ")

print("SE ha quedado sin dinero")