" Procedemos a calcular cuantas vocales tiene cada frase  insertada por el usuario y en listarlas"

frase=input("Ingrese una frase: ")
for indice in range(len(frase)):
    print(indice,"=",frase[indice])
    for car in frase:
        if car in ("a", "e", "i", "o", "u","A", "E", "I", "O", "U"):
             if car in ("A", "E", "I", "O", "U"):
                continue
             else:
              cvoc = cvoc+1
print ("Cantidad de vocales:{}".format(cvoc))
[car for car in["a", "e", "i", "o", "u"] if car not in ("a", "i", "o")]

