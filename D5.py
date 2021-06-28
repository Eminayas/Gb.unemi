""" Dado el sueldo de un empleado, 
encontrar el nuevo sueldo si obtiene un aumento del 10% si su sueldo es inferior a $600, 
en caso contrario no tendrá aumento. """


class Ejemplo5:
    def __init__(self):
        pass
    
    def aumentosuel(self):
        SI = float(input("Ingrese el valor del Sueldo que gana:  "))
        if SI <= 600:
            print("Se le otrogara un aumento del 10%, a su sueldo actual")
            NSI = SI  * 0.1
            NS = NSI + SI
            print("Su nuevo sueldo es: {} ".format(NS))   
        else:
            print("Su sueldo es: {} ".format(SI))
        
eje1 = Ejemplo5()
eje1.aumentosuel()