#Una compañía de transporte internacional tiene servicio en algunos países de América del 
#Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte 
#se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la 
#tabla:
#Zona Ubicación Costo/gramo
#1 América del Norte 24.00 euros
#2 América Central 20.00 euros
#3 América del Sur 21.00 euros
#4 Europa 10.00 euros
#5 Asia 18.00 euros
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son 
#transportados, esto por cuestiones de logística y de seguridad.
#Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el 
#rechazo de la entrega.

zona=int(input("Introduce la zona a la que quieres enviar el paquete\n1.America del Norte\n2.America Central\n3.America del Sur\n4.Europa\n5.Asia\n"))
#peso=float(input("Introduce el peso del paquete en gramos\n"))

if zona>0 and zona<=5:
    peso=float(input("Introduce el peso del paquete en gramos\n"))
    if peso>0 and peso<=5000:
        if zona==1:
            print("El precio del envio es de",peso*24,"euros")
        elif zona==2:
            print("El precio del envio es de",peso*20,"euros")
        elif zona==3:
            print("El precio del envio es de",peso*21,"euros")
        elif zona==4:
            print("El precio del envio es de",peso*10,"euros")
        elif zona==5:
            print("El precio del envio es de",peso*18,"euros")
    else:
        print("Lo sentimos, su paquete supera el limite de 5 kg")
else:
    print("ERROR: Introduzca una zona valida")