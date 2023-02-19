#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. 
#Ejemplo, si se introduce 23 que muestre 32.

numero=((input("dime un numero\n")))

#lo pasamos a entero
numero=int(numero)

#calculamos cada cifra
a=(numero%10)
b=(numero/10)

#quitamos los decimales
a=int(a)
b=int(b)

#lo pasamos a caracteres
a=str(a)
b=str(b)

#imprimimos el resultado
print(b)
print("Ohh",numero,"el invertido de ese numero es el",a+b)

