
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se
#clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, 
#ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la 
#uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
#se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de 
#tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos 
#cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

base=1
uvapedido=input("Ingrese el tipo de uva que quiere comprar(A1/A2/B1/B2): ")
cantidadpedido=int(input("Ingrese la cantidad de kilos que quiere comprar: "))

if uvapedido=="A1":
    pvp=base+0.20
    print ("El precio total es: ",cantidadpedido*pvp,"euros")
elif uvapedido=="A2":
    pvp=base+0.30
    print ("El precio total es: ",cantidadpedido*pvp,"euros")
elif uvapedido=="B1":
    pvp=base-0.30
    print ("El precio total es: ",cantidadpedido*pvp,"euros")
elif uvapedido=="B2":
    pvp=base-0.50
    print ("El precio total es: ",cantidadpedido*pvp,"euros")