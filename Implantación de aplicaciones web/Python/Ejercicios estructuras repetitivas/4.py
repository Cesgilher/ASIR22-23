#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a 
#introducir). El programa debe informar de cuantos números introducidos son mayores que 0, 
#menores que 0 e iguales a 0.

cantidadnumeros=int(input("Cuantos numeros vas a introducir  "))
iguales=0
mayores=0
menores=0
for i in range(0,cantidadnumeros):
    x=int(input("dime un numero  "))
    if x==0:
        iguales+=1
    elif x>0:
        mayores+=1
    else:
        menores+=1

print(iguales,"numeros son iguales a 0")
print(menores,"numeros son menores que 0")
print(mayores,"numeros son mayores que 0")

