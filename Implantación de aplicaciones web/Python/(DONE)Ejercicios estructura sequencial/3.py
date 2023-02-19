#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

a=int(input("cateto a\n"))
b=int(input("cateto b\n"))
print("a cuadrado:",a*a)
print("b cuadrado:",b*b)
hipotenusa=(((a**2)+(b**2))**1/2)

print("la hipotenusa del triangulo es:",hipotenusa)