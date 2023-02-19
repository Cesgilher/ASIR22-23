#Escribir un programa que imprima todos los números pares entre dos números que se le 
#pidan al usuario

x=int(input("Dime el primer valor  "))
y=int(input("Dime el segundo valor  "))

for i in range(x,y):
    if i%2==0:
        print(i)