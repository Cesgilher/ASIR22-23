#Algoritmo que pida un número y diga si es positivo, negativo o 0.

numero1=int(input("Dime un numero: "))

if numero1==0:
    print("El numero es 0")
elif numero1<0:
    print("El numero es negativo")
else:
    print("El numero es positivo")