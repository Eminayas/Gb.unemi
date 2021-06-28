""" En una tienda se ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber 
cuánto deberá pagar finalmente por su compra.
 
 	
Resolveremos el ejercicio, aplicando los pasos de la metodología de la solución de un problema:
DEFINICIÓN DEL PROBLEMA:
Obtener la cantidad de dinero que tendrá que pagar el cliente, si la tienda ofrece un 15% de descuento sobre el total de la compra.

 

ANÁLISIS DEL PROBLEMA:
Para obtener el descuento es necesario conocer la cantidad total de la compra, y sobre ésta aplicar el 15%. 
Posteriormente, este descuento deberá ser sustraído de la cantidad total de la compra para así obtener la cantidad con descuento,
que es la que el cliente pagará.

Pasos que se deben realizar:
Salidas:   Cantidad a pagar
Entradas: Total de la compra

Datos adicionales: el descuento equivale al 15% sobre el total de la compra.
Aplicar las siguientes fórmulas:
     Descuento = total de la compra * 0.15
      Cantidad a pagar = total de la compra – descuento """



class Ejemplo1:
    def __init__(self):
        pass
    
    def pagotoal(self):
        tc = float(input("Ingrese total compra:  "))
        des = tc*0.15
        pago = tc-des
        print("Tcompras: {}, Des:{}, Valor a Pagar:{}".format(tc,des,pago))
        
eje1 = Ejemplo1()
eje1.pagotoal()