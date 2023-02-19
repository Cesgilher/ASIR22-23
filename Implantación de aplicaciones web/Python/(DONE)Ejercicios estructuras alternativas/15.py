#El director de una escuela está organizando un viaje de estudios, y requiere determinar 
#cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el 
#servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada 
#alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 
#euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar 
#el número de alumnos.

numeroalumnos = int(input("Introduce el numero de alumnos: "))

if numeroalumnos >= 100:
    print("El costo por alumno es de 65 euros")
    print("El total a pagar a la compañia de autobuses es de",numeroalumnos*65,"euros")
    
elif numeroalumnos >= 50 and numeroalumnos <= 99:
    print("El costo por alumno es de 70 euros")
    print("El total a pagar a la compañia de autobuses es de",numeroalumnos*70,"euros")

elif numeroalumnos >= 30 and numeroalumnos <= 49:
    print("El costo por alumno es de 95 euros")
    print("El total a pagar a la compañia de autubuses es de",numeroalumnos*95,"euros")

else:
    print("El total a pagar a la compañia de autobuses es de 4000 euros")
    