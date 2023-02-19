#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.



a=input("dame una letra  ")
print (a.upper())
print(a==a.upper)
if a==a.upper:
    print("es una mayuscula")
else:
    print("es una minuscula")