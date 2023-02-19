
#pedir numero trabajadores
numeroTrabajadores = int(input("¿Cuantos trabajadores hay en la empresa? "))

costeSemanalEmpresa = 0

for i in range(numeroTrabajadores):
    #pedir sueldo un trabajador
    print("Trabajador "+str(i+1))
    sueldo = float(input("¿Cual es su sueldo por hora? "))
    #pedir numero de dias trabajados
    diasTrabajados = int(input("¿Cuantos dias ha trabajado esta semana? "))
    #pedir horas cada dia
    horasTrabajadasPorSemana=0
    for j in range(diasTrabajados):
        horasTrabajadasPorDia = float(input("¿Cuantas horas ha hecho el dia "+str(j+1)+" ? "))
        horasTrabajadasPorSemana+=horasTrabajadasPorDia
    print("Horas trabajadas por el trabajador"+str(i+1)+" esta semana: "+str(horasTrabajadasPorSemana))        
    sueldoDeUnTrabajador = sueldo*horasTrabajadasPorSemana
    print("El sueldo de este trabajador es: "+str(sueldo)+"x"+str(horasTrabajadasPorSemana)+"="+str(sueldoDeUnTrabajador)+"€")
    costeSemanalEmpresa += sueldoDeUnTrabajador

print("El coste semanal de la empresa es "+str(costeSemanalEmpresa)+"€")