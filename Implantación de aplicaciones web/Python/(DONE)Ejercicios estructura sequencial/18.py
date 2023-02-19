#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
nombre=input("Ingrese su nombre\n")
apellido1=input("Ingrese su primer apellido\n")
apellido2=input("Ingrese su segundo apellido\n")

iniciales=(nombre.upper()[0:1]+"."+apellido1.upper()[0:1]+"."+apellido2.upper()[0:1]+".")
print("Sus iniciales son: "+iniciales)