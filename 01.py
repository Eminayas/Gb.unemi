x=int(input("Ingrese un numero entero: "))
if x<0: 
    x = 0
    ptint("Negativo cambiando a cero")
elif x== 0: 
    print ("Cero")
elif x== 1:
    print ("Uno")
else:
    print ("Ninguna opcion")

print("Ok") if type(x) == int else print ("-")
