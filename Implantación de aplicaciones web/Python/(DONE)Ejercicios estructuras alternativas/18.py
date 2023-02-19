#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día 
#correspondiente. Si introducimos otro número nos da un error.
dia=int(input("dia de la semana"))

if dia>1 or dia<7:
    if dia==1:
        print("Lunes")
    elif dia==2:
        print("Martes")
    elif dia==3:
        print("Miercoles")
    elif dia==4:
        print("Jueves")
    elif dia==5:
        print("Viernes")
    elif dia==6:
        print("Sabado")    
    elif dia==7:
        print("Domingo")
    else:
        print("ERROR: dia no valido")
