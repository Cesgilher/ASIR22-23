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
producto5=1
descuento=1

#hacemos la consulta al usuario
print("Bienvenido al supermercado, estos son los productos disponibles: ")
print("1. Producto1:",producto1,"€. 20% de descuento los lunes.")
print("2. Producto2:",producto2,"€.")
print("3. Producto3:",producto3,"€. 2x1 los miercoles.")
print("4. Producto4:",producto4,"€.")
print("5. Producto5:",producto5,"€.")
print("Martes: 20% extra en todo por alelao.")
print("Viernes: todos los productos tienen un 70% de descuento.")


dia=input("Qué dia es? ")
cliente=input("¿Quien es usted? ")
x=input("Desea comprar algun producto? ")
total=0
parcial=0
if dia.lower()!="domingo":
    while x.lower()=="si":
        eleccion=input("Elige el producto que desea adquirir: ")
        cantidad=int(input("¿Cuantas unidades desea? "))
    #declaramos las condiciones, añadiendo los descuentos de cada dia al producto correspondiente
        if dia.lower()=="lunes" and eleccion.lower()=="producto1":  
            descuento=0.8
        elif dia.lower()=="martes":
            descuento=1.2
        elif dia.lower()=="miercoles" and eleccion.lower()=="producto3":
            cantidad=cantidad//2+cantidad%2    
        elif dia.lower()=="viernes":
            descuento=0.3
    #declaramos las condiciones para los clientes vip
        if cliente.lower()=="carlos" or cliente.lower()=="ines" and (eleccion.lower()=="producto1" or eleccion.lower()=="producto2" or eleccion.lower()=="producto3"):
            descuento-=0.1
        elif cliente.lower()=="srmuro":
            descuento=1.5
            if dia.lower()=="martes":
                descuento+=0.2

    #declaramos las igualdades entre las elecciones y los productos

        if eleccion.lower()=="producto1":
                eleccion=producto1
        elif eleccion.lower()=="producto2":
                eleccion=producto2
        elif eleccion.lower()=="producto3":
                eleccion=producto3
        elif eleccion.lower()=="producto4":
                eleccion=producto4
        elif eleccion.lower()=="producto5":
                eleccion=producto5
        else:
            print("No existe ese producto")

        parcial=eleccion*cantidad*descuento
        total+=parcial
        print(f"Este producto te costará {parcial}€")
        print (f"El precio total es de {total}€")
        x=input("Quiere comprar algo mas? ")
    
    print("Gracias por su compra, vuelva pronto")
else:
    print("Hoy es domingo, vuelva mañana.")
    exit()





























#declaramos el precio final
#if cliente.lower()=="srmuro":
#   print("Hola "+cliente+". Por parguelas te cobro un 50% mas.")
#     print("El coste total es de",round(total, 2),"€.")

#  elif cliente.lower()=="carlos" or cliente.lower()=="ines":
#  print("Hola "+cliente+". Tiene un 10% de descuento adicional por ser cliente vip.")
#       print("El coste tras aplicar el descuento es de",round(total, 2),"€.")
#else:
#        print("El coste total es de",round(total, 2),"€.")

#print("Gracias por su compra.")
#exit()    
