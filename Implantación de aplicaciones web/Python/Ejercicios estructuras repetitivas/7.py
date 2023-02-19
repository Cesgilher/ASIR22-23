#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por 
#teclado.
x=int(input("dime un numero  "))

for i in range(0,11):
    print(x,"*",i,"=",x*i)