#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5

for i in range(1,6):
    print("Tabla de multiplicar del",i)
    for j in range(0,11):
        print(i,"*",j,"=",j*i)