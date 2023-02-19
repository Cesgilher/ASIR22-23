#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.

dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))
año = int(input("Introduce el año: "))

 
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia > 0 and dia <= 31:
        print("La fecha es correcta")
    else: 
        print("La fecha es incorrecta")     

 if mes == 2:
    if (año//400) or (año//4 and not año//100):
        
        if dia > 0 and dia <= 29:
            print("La fecha es correcta")
        else: 
            print("La fecha es incorrecta")
    elif dia>0 and dia<29:
        print("La fecha es correcta")
    else:
        print("La fecha es incorrecta")   

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 0 and dia <= 30:
        print("La fecha es correcta")
else:
        print("La fecha es incorrecta")     