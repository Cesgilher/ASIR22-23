#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es
#cero, o un mensaje de aviso en caso contrario.

from re import L


numero1=int(input("ingrese un numero "))
numero2=int(input("ingrese otro numero "))

if numero2==0:
    print("No se puede dividir entre cero, alelao")
else:
    print("el resultado de la division es:",(numero1/numero2))