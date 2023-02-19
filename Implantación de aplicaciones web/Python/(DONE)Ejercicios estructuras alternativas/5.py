#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido 
#“pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error

from cgitb import reset
from logging.config import stopListening


usuario=input("Nombre de usuario: ")
contraseña=input("Contraseña: ")

if usuario=="pepe" and contraseña=="asdasd":
    print("Has entrado al sistema")
else:
    print("Error, vuelve a intenterlo")
    