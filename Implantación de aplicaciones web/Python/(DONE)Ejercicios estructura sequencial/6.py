#Calcular la media de tres números pedidos por teclado.
import statistics
a=int(input("dime un numero\n"))
b=int(input("dime otro\n"))
c=int(input("venga, un tercero\n"))
data=[a,b,c]
media=statistics.mean(data)
print("la media es:", media)
