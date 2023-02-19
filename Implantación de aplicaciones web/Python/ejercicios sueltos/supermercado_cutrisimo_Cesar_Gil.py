#sin ifs
#con 5 productos
#los precios puestos a fuego en el codigo

producto1=3
producto2=1.2
producto3=0.6
producto4=2.7
producto5=1.5

#preguntas cantidades de cada uno

cantidad1=int(input("¿Cuantos productos del tipo 1 desea?"))
cantidad2=int(input("¿Cuantos productos del tipo 2 desea?"))
cantidad3=int(input("¿Cuantos productos del tipo 3 desea?"))
cantidad4=int(input("¿Cuantos productos del tipo 4 desea?"))
cantidad5=int(input("¿Cuantos productos del tipo 5 desea?"))

#calcular precio final

precio1= producto1*cantidad1
precio2= producto2*cantidad2
precio3= producto3*cantidad3
precio4= producto4*cantidad4
precio5= producto5*cantidad5

preciofinal=precio1+precio2+precio3+precio4+precio5

print("El precio final es de",preciofinal,"euros")
