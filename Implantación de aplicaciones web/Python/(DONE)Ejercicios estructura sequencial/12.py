#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
#Calcula y muestra la distancia entre ellos

x1=int(input("coodernada x1\n"))
y1=int(input("coodernada y1\n"))
x2=int(input("coodernada x2\n"))
y2=int(input("coodernada y2\n"))

dif=(((x1-x2)**2+(y1-y2)**2)**(1/2))

print("la distancia entre los puntos es =",dif)
