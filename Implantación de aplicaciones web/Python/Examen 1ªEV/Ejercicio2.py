
asistenciaNeutralTotal=0
asistenciaTotal=0
for i in range(7):
    print("Día",i+1)
    asistenciaTotalDiaria=0
    for j in range(4):
        asistenciaPorPartidoTotal=0
        print("Partido",j+1)
        #Pedimos la asistencia diaria
        asistenciaPorPartidoLocal=int(input("Cuantos aficionados del equipo local han ido al partido? "))
        asistenciaPorPartidoVisitante=int(input("Cuantos aficionados del equipo visitante han ido al partido? "))
        asistenciaPorPartidoNeutral=int(input("Cuantos aficionados neutrales han ido al partido? "))
        
        #Vamos sumando los valores de cada partido
        asistenciaPorPartidoTotal+=asistenciaPorPartidoVisitante+asistenciaPorPartidoNeutral+asistenciaPorPartidoLocal
        mediaNeutralDiaria=asistenciaPorPartidoNeutral/asistenciaPorPartidoTotal
        asistenciaTotalDiaria+=asistenciaPorPartidoTotal
        
        #Vamos sumando la asistencia neutral de cada partido a la asistencia total de los 7 dias
        asistenciaNeutralTotal+=asistenciaPorPartidoNeutral
    
    #Vamos sumando el totla de cada dia al total semanal
    asistenciaTotal+=asistenciaTotalDiaria
    print("La asistencia diaria es: ",asistenciaTotalDiaria)
    print(f"La media de Qataries diaria es de: {(mediaNeutralDiaria*100):.1f}%")
print("En total han asistido ",asistenciaTotal," aficionados al mundial")
print("En total han asistido ",asistenciaNeutralTotal," qataries al mundial")
