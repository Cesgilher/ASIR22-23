#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha
#calificación se compone de los siguientes porcentajes:
#•55% del promedio de sus tres calificaciones parciales.
#•30% de la calificación del examen final.
#•15% de la calificación de un trabajo final.
parciales=float(input("nota media de los parciales\n"))
examenfinal=float(input("nota del examen final\n"))
trabajofinal=float(input("nota del trabajo final\n"))
notafinal=(parciales*0.55)+(examenfinal*0.3)+(trabajofinal*0.15)

print("Tu nota final es un",notafinal)
