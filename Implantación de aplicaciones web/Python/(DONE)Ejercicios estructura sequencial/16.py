#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una 
#distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para 
#ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con 
#esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro

v1=input("Velocidad del coche que va delante(km/h)?\n")
v2=input("Velocidad del coche que va detras(km/h)?\n")
x0=input("A que distancia están(km)?\n")

#lo pasamos a decimal
v1=float(v1)
v2=float(v2)
x0=float(x0)

#lo pasamos de km/h a m/s
v1=(v1/3.6)
v2=(v2/3.6)
x0=(1000*x0)

#calculamos el momento de cruce
#x=x0+v*t
#xv1=(100+v1*t)
#xv2=(v2*t)
#xv1=xv2=v1*t= 100+v1*t-v2*t=0
#(v1-v2)*t=-100
#t=-100/(v1-v2)

t=(-x0/(v1-v2))

#pasamos el tiempo a minutos
t=(t/60)

print(t)
