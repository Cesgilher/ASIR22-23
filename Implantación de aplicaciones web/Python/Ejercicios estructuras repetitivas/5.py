#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso 
#contrario, el programa termina cuando se introduce un espacio.

letra=input("dime una letra  ")

while letra!=" ":
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        print("VOCAAAAL")
    else:
        print("CONSONANTEEE")
    letra=input("dime otra letra  ")
    