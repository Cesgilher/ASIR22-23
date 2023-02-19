
x=int(input("dime un numero  "))
y=0
intentos=0
while x!=0:
    y+=x
    intentos+=1
    x=int(input("dime otro numero  "))

print(y)
print(y/intentos)