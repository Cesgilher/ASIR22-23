#Supermercado, 5 productos(1,2,3,4,5), el usuario compra solo dos y tiene que elegirlos. 
#Mostrar un menu con los productos y si precio y que eliga
#- Que segun el dia de la semana hay descuentos en algun producto.  
# El lunes el producto1 tiene 20%, el miercoles hay 2x1 del producto3, el viernes hay locura, 70% en todos. Los domingos no se abre.
#-En el menu de productos tienes que avisar los descuentos que haya.
#- Clientes vip, carlos, ines, en el producto 1,2,3 descuento adicional del 10%
#-Cliente pufo, SrMuro paga un 50% mas, y no tiene descuentos.
#- Los martes es el día de los border lines,  la factura se sube 20%.


#declaramos las variables
producto1=1.5
producto2=2.1
producto3=5.5
producto4=0.9
producto5=3.3
descuento=1
#hacemos la consulta al usuario
print("Bienvenido al supermercado, estos son los productos disponibles: ")
print("1. Producto1:",producto1,"€.")
print("2. Producto2:",producto2,"€.")
print("3. Producto3:",producto3,"€.")
print("4. Producto4:",producto4,"€.")
print("5. Producto5:",producto5,"€.")
print("Lunes: el producto1 tiene un 20% de descuento.")
print("Martes: 20% extra en todo por alelao.")
print("Miercoles: el producto3 tiene 2x1.")
print("Jueves y sabados: no hay descuentos.")
print("Viernes: todos los productos tienen un 70% de descuento.")
print("Domingos:CERRADO.")

dia=input("Qué dia es ")
cliente=input("¿Quien es usted? ")
eleccion1=input("Elige el primer producto que desea adquirir: ")
cantidad1=int(input("¿Cuantas unidades desea? "))


#declaramos las condiciones, añadiendo los descuentos de cada dia al producto correspondiente
if dia==1:  
    if cliente.lower=="SrMuro" or cliente=="Srmuro" or cliente=="srmuro":
        
    elif cliente=="carlos" or cliente=="Carlos" or cliente=="Ines" or cliente=="ines":
        producto1=producto1*0.7
        
    else:
        producto1=producto1*0.8
elif dia==2:
    if cliente=="SrMuro" or cliente=="Srmuro" or cliente=="srmuro":
        producto1=producto1*1.5
        producto2=producto2*1.5
        producto3=producto3*1.5
        producto4=producto4*1.5
        producto5=producto5*1.5
    elif cliente=="carlos" or cliente=="Carlos" or cliente=="Ines" or cliente=="ines":
        x=1
    else:
        producto1=producto1*1.2
        producto2=producto2*1.2
        producto3=producto3*1.2
        producto4=producto4*1.2
        producto5=producto5*1.2
        
elif dia==5:
    if cliente=="SrMuro" or cliente=="Srmuro" or cliente=="srmuro":
        producto1=producto1*1.5
        producto2=producto2*1.5
        producto3=producto3*1.5
        producto4=producto4*1.5
        producto5=producto5*1.5
    else:
        producto1=producto1*0.7
        producto2=producto2*0.7
        producto3=producto3*0.7
        producto4=producto4*0.7
        producto5=producto5*0.7

#declaramos las igualdades entre las elecciones y los productos

#primero para eleccion1
if eleccion1=="producto1" or eleccion1=="Producto1":
    eleccion1=producto1
    
elif eleccion1=="producto2" or eleccion1=="Producto2":
    eleccion1=producto2
elif eleccion1=="producto3" or eleccion1=="Producto3":
    eleccion1=producto3
elif eleccion1=="producto4" or eleccion1=="Producto4":
    eleccion1=producto4
elif eleccion1=="producto5" or eleccion1=="Producto5":
    eleccion1=producto5
else:
    print("No existe ese producto")
    exit()
#declaramos el 2x1 para la eleccion1
if dia==3 and eleccion1==producto3:
    cantidad1=(cantidad1//2+cantidad1%2)

#ahora para eleccion2
if eleccion2=="producto1" or eleccion2=="Producto1":
    eleccion2=producto1
elif eleccion2=="producto2" or eleccion2=="Producto2":
    eleccion2=producto2
elif eleccion2=="producto3" or eleccion2=="Producto3":
    eleccion2=producto3
elif eleccion2=="producto4" or eleccion2=="Producto4":
    eleccion2=producto4
elif eleccion2=="producto5" or eleccion2=="Producto5":
    eleccion2=producto5
else:
    print("No existe ese producto")
    exit()
#declaramos el 2x1 para la eleccion2
if dia==3 and eleccion2==producto3:
    cantidad2=(cantidad2//2+cantidad2%2)


#calculamos el prcio total sin tener en cuenta quien es el cliente
print("El coste total es de",round(total, 2),"€.")

#ahora hacemos la consulta para saber si es cliente vip o no


#en fincion de si es cliente vip o no, aplicamos unos descuentos o otros

print("Hola "+cliente+". Tiene un 10% de descuento adicional por ser cliente vip.")
total=eleccion1*cantidad1+eleccion2*cantidad2
print("El coste tras aplicar el descuento es de",round(total, 2),"€.")