""" Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. 
El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y 
el total que recibirá en el mes tomando en cuenta su sueldo base y sus comisiones.
 	
DEFINICIÓN DEL PROBLEMA:
Obtener la cantidad de dinero que recibirá un vendedor por concepto de comisiones por tres ventas realizadas en el mes, 
y el total que recibirá en el mes por sueldo y comisión. Se sabe que el vendedor recibe un sueldo base 
y un 10% extra por comisiones de todas sus ventas.

ANÁLISIS DEL PROBLEMA:
Para obtener la comisión y la cantidad que recibirá el vendedor, se necesita realizar lo siguiente:
Para obtener la cantidad total de ventas hay que conocer la cantidad de cada una de sus ventas en                                            el mes y sumarlas. Posteriormente, sobre el total de las ventas se debe aplicar el 10% para obtener la comisión. Por último, para obtener el total de dinero que debe recibir el vendedor hay que sumarle al sueldo base la comisión.

Pasos que se deben realizar:
Salidas:   Cantidad a recibir por comisión, cantidad total a recibir
Entradas: cantidad de venta 1, 2 y 3, sueldo base
Datos adicionales: el descuento de 10% se aplicará sobre el total de las ventas del mes """


class Ejemplo2:
    def __init__(self):
        pass
    
    def vendedor(self):
        SB = float(input("Ingrese su salario basico mensual a recibir:  "))
        V1 = float(input("Ingrese el valor de la primera venta:  "))
        V2 = float(input("Ingrese el valor de la segunda venta:  "))
        V3 = float(input("Ingrese el valor de la tercera venta:  "))
        TV = (V1+V2+V3)
        C = TV*0.1
        TR = SB + C
        print("Salario Basico a recibir más la comision: {}, Comision a Recibir por ventas: {}, Total de Ventas:{} ".format(TR,C,TV))
        
eje1 = Ejemplo2()
eje1.vendedor()