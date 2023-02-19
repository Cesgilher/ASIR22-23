#Escribe un programa que dados dos números, uno real (base) y un entero positivo 
#(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador 
#de potencia.

x=int(input("dime un numero  "))
y=int(input("dime su exponente  "))
f=1
for i in range(1,y+1):
    f*=x
print(f)