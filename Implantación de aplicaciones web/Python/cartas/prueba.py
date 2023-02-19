

print("┌-┐\n└-┘")


for j in range(0,2):
            for h in range(0,4):
                if tirada[0].valor.value==1:              #si sale un uno arriba lo coloco en mesa
                    if tirada[0].palo.value==h:
                        cartasEnMesa[h]=tirada[0]
                        del tirada[0]
                    
                elif hasattr(cartasEnMesa[h], "valor"):#si sale el siguiente numero al que hay en mesa , lo coloca
                    if tirada[0].palo.value==h and tirada[0].valor.value==(cartasEnMesa[h].valor.value+1):
                        cartasEnMesa[h]=tirada[0]
                        del tirada[0]

for h in range(0,2):
            
            
            for j in range(0,4):#j=0
                if tirada[0].valor.value==1:              #si sale un uno arriba lo coloco en mesa
                    if tirada[0].palo.value==j:
                        cartasEnMesa[j]=tirada[0]
                        del tirada[0]
                    
                elif hasattr(cartasEnMesa[j], "valor"):#si sale el siguiente numero al que hay en mesa , lo coloca
                    if tirada[0].palo.value==j and tirada[0].valor.value==(cartasEnMesa[j].valor.value+1):
                        cartasEnMesa[j]=tirada[0]
                        del(tirada[0])
