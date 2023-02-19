#Escribir un programa que pregunte al usuario su nombre, y luego lo salude

#hay varias formas de hacer este ejercicio
#primera
from unicodedata import name


print("Hola",input("¿Cómo te llamas?\n"))


#segunda
name=input("¿Cómo te llamas?\n")
print("Hola", name)
#esta forma es la mas util porque asi el valor queda almacenado en una variable y pudes llamarlo mas veces