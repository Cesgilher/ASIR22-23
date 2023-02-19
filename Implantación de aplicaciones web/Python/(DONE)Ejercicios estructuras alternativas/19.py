#Escribe un programa que pida un número entero entre uno y doce e imprima el número de 
#días que tiene el mes correspondiente.

mes=int(input("Dime que mes del año quieres saber"))

if mes>0 and mes<13:
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            print("El mes tiene 31 dias.")
        
    elif mes==2:
        print("El mes tiene 28 dias, salvo si es año bisiesto, en cuyo caso tiene 29.")
    else:
        print("El mes tiene 30 dias.")
else:
        print("ERROR: El valor no es correcto")
    