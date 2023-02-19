#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un 
#dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara 
#opuesta al resultado obtenido.
#•Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y
#3-4.
#•Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará
#el mensaje: “ERROR: número incorrecto.”.
resultado=int(input("Introduce el resultado del dado: "))

if resultado>0 or resultado<6:
    if resultado==1:
        print("seis")
    elif resultado==2:
        print("cinco")
    elif resultado==3:
        print("cuatro")
    elif resultado==4:
        print("tres")
    elif resultado==5:
        print("dos")
    elif resultado==6:
        print("uno") 
    else:
        print("ERROR: numero incorrecto")