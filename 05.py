"Funciones sin retorno"

def vocales(frase):
     for car in frase:
         if car in('a','e','i','o','u'):
            print(car)

"Llamada a funcion"
oracion = input("Ingrese oracion: ")
vocales(oracion.lower())


"Funcion con retorno de valor"
def promedio(notas):
    summ = 0
    for n in notas:
        summ += n
    return summ / len(notas)

# llamada a funcion
listanotas = [2, 4, 6, 8, 10]
prom = promedio(listanotas)
print("Promedio: {} = {}".format(listanotas, prom))