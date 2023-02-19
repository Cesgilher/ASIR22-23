#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas
#horas y minutos corresponde.
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

min=int(input("Cuantos minutos deseas convertir a horas\n"))
resto=(min%60)
hora=((min-resto)/60)
print(min,"minutos son:",hora,"horas y",resto,"minutos")

