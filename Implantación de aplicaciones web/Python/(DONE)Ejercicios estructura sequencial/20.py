#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de 
#pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos)

a=int(input("Cuantas monedas de 2€ tienes?\n"))
b=int(input("Cuantas monedas de 1€ tienes?\n"))
c=int(input("Cuantas monedas de 50 centimos tienes?\n"))
d=int(input("Cuantas monedas de 20 centimos tienes?\n"))
e=int(input("Cuantas monedas de 10 centimos tienes?\n"))

#pasamos todo a centimos
a=a*200
b=b*100
c=c*50
d=d*20
e=e*10

total=a+b+c+d+e
euros=int(total/100)
cents=int(total%100) #tambien se podria obtener mediante cents=total-euros
print("Tienes acumulados un total de",euros,"euros y",cents,"centimos.")