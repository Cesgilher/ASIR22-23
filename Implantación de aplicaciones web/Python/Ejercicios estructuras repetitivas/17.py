#Una empresa les paga a sus empleados con base en las horas trabajadas en la semana. 
#Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo 
#para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la 
#empresa por los N empleados.

pagoEmpresa=0
salarioHora=int(input("Cual es el salario en €/hora?\n"))
nºdeTrabajadores=int(input("Cuantos trabajadores tiene su empresa?\n"))
for i in range(1,nºdeTrabajadores+1):
    nºdeDias=int(input("Indique el numero de dias trabajados por el trabajador "+str(i)+"\n"))
    nºdeHoras=float(input("Cuantas horas ha trabajado al dia?\n"))
    salarioTrabajador=nºdeDias*nºdeHoras*salarioHora
    pagoEmpresa+=salarioTrabajador
    print("Se le debe un total de "+str(salarioTrabajador)+" al trabajador "+str(i))
    print("El total a pagar por la empresa es de "+ str(pagoEmpresa))