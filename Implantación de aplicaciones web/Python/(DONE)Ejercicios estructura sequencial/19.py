#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada 
#respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el 
#resultado obtenido por el estudiante.

#Partiendo de esta base supondremos que el examen tiene un máximo de 20 preguntas,
#para que los valores esté comprendidos entre 0 y 100 puntos, siendo 0 un 0 y 100 un diez en la nota del examen
correctas=int(input("Nº de respuestas correctas\n"))
erroneas=int(input("Nº de respuestas erroneas\n"))
nulas=input("Nº de respuestas en blanco\n")
#realmente las preguntas en blanco no hace falta registrarlas porque no juegan ningun papel en la nota final
nota=(5*correctas-erroneas)/10
print("Tu nota final es:",nota)