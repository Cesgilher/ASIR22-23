from domain.modelo.baraja import Baraja
from domain.servicios.servicios_cartas import ServiciosCartas
from domain.modelo.Carta import Carta

def main():
    serviciosCartas = ServiciosCartas()
    baraja : Baraja = serviciosCartas.crear_baraja()
    serviciosCartas.mezclar_baraja(baraja)
    cartasEnMesa: list[Carta]=[]
    cartasEnMesa=["┌-┐\n└-┘" for _ in range(4)] #asi asigno un valor inicial vacio al array de cartas que hay en mesa
    ronda=0 # asi defino en que ronda estamos, siendo una ronda cada vez que mse recogen las cartsa y se vuelven a sacar.
    while len(baraja.cartas):# asi me aseguro de que se ejecute mientras queden cartas en la baraja
        ronda+=1
    
        print("Ronda:",ronda)
        nuevaBaraja: list[Carta]=[]
        for i in range (0,len(baraja.cartas),2): #esto es para coger 2 cartas en cada turno
            tirada: list[Carta] = []
            print("Tirada",(i//2)+1)
            if i+1==len(baraja.cartas):
                tirada.append(baraja.cartas[i])
            else:
                for j in range(0,2):
                    tirada.append(baraja.cartas[i+1-j])# esto es para coger las cartas de atrás hacia delante
                for j in range(0,len(tirada)):
                    print(tirada[j])
            
            

            for h in range(0,2):
                for j in range(0,4):#j=0
                    if tirada:
                        if tirada[0].valor.value==1:              #si sale un uno arriba lo coloco en mesa
                            if tirada[0].palo.value==j:
                                cartasEnMesa[j]=tirada[0]
                                del tirada[0]
                
                        elif hasattr(cartasEnMesa[j], "valor"):#Por cada palo si sale el siguiente numero al que hay en mesa , lo coloca
                            if tirada[0].palo.value==j and tirada[0].valor.value==(cartasEnMesa[j].valor.value+1):
                                cartasEnMesa[j]=tirada[0]
                                del(tirada[0])
            tirada.reverse()
            if tirada:        
                for j in range (0,len(tirada)):
                    nuevaBaraja.append(tirada[j])
                

            print("------------")
            print("Cartas en mesa")
            print("------------")
            for j in range(0,4):
                print(cartasEnMesa[j])
            print("------------")
        #for carta in baraja.cartas:
            #print(carta)
        if len(nuevaBaraja)==len(baraja.cartas):
            print("No puedo colocar ninguna carta más. Reinicia la partida")
            exit()
        while baraja.cartas:
            del baraja.cartas[0]
            
        
        for j in range(0,len(nuevaBaraja)):
            #print(nuevaBaraja[j])
            baraja.cartas.append(nuevaBaraja[j])
        #print("------------")
        for j in range(0,len(baraja.cartas)):
            print(baraja.cartas[j])
        
    
