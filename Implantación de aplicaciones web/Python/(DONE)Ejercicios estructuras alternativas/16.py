#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro 
#es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, 
#los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del 
#décimo minuto, 50 céntimos.
#Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de 
#mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe 
#pagar por cada concepto una persona que realiza una llamada.

minutos=int(input("Introduce los minutos de la llamada: "))
turno=input("Introduce el turno de la llamada (M/T): ")
dia=input("Introduce el dia de la llamada (D/L): ")

if minutos <= 5:
    precio=1
elif minutos <= 8:
    precio=1.80
elif minutos <= 10:
    precio=2.50
else:
    precio=2.50+(minutos-10)*0.50

if dia == "D":
    precio=precio*1.03
elif turno == "M":
    precio=precio*1.15
else:
    precio=precio*1.10

print("El precio de la llamada es de", precio, "euros")