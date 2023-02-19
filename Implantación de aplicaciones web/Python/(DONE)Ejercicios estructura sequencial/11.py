#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su
#diferencia, de modo que el resultado sea siempre positivo).
a=int(input("dime un numero\n"))
b=int(input("dime otro numero\n"))

if (a>b):
    dif=(a-b)
else:
    dif=(b-a)

print("la diferencia entre a y b es =",dif)