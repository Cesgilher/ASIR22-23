#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de 
#viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la 
#hora de llegada a la ciudad B

hora_de_salida=input("¿A que hora sale de la ciudad A el ciclista(HH:MM:SS)?\n")

t=int(input("¿Cuántos segundos tarda el ciclista en llegar a la cuidad B?\n"))

#obtenemos los respectivos valores de horas, minutos y segundos a partir de la hora dada por el usuario
hora0=hora_de_salida[0:2]
minuto0=hora_de_salida[3:5]
segundo0=hora_de_salida[6:8]

#pasamos los valores iniciales a enteros
hora0=int(hora0)
minuto0=int(minuto0)
segundo0=int(segundo0)

#calculamos el tiempo que tarda en realizar el desplazamiento
hora1=int(t/3600)
minuto1=int((t%3600)/60)
segundo1=int((t%3600)%60)
duracion_trayecto=(str(hora1)+str(minuto1)+str(segundo1))

#obtenemos la hora ala que llega a su destino
hora2=hora0+hora1
minuto2=minuto0+minuto1
segundo2=segundo0+segundo1

#ajustamos los resultados para que sigan el formato horario sexagesimal
horaf=((hora2+int(minuto2/60))%24)
minutof=((minuto2+int(segundo2/60))%60)
segundof=(segundo2%60)

#convertimos los datos y los imprimimos por pantalla
hora_de_llegada=(str(horaf)+":"+str(minutof)+":"+str(segundof))
print("Hora de salida:",hora_de_salida)
print("Hora de llegada: "+hora_de_llegada+".")