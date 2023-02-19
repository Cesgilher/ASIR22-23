#Calcular el perímetro y área de un rectángulo dada su base y su altura.

base=int(input("¿Cúal es la base del rectángulo?\n"))
altura=int(input("¿Y la altura?\n"))
perimetro=(base*2+altura*2)
area=(base*altura)

print("Su rectángulo tiene un area de",area,"cm^2 y un perímetro de",perimetro,"cm")