#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el
#vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres
#ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
#base y comisiones.

base=int(input("Sueldo base\n"))
venta1=int(input("Precio de la primera venta\n"))
venta2=int(input("Precio de la segunda venta\n"))
venta3=int(input("Precio de la tercera venta\n"))
comision=((venta1+venta2+venta3)*0.1)
salario=(base+comision)
print("tu comision de este mes es:",comision)
print("tu salario de este mes es:", salario)