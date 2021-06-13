class Ciclo: 
    
    def __init__(self,num=10):
        self.numero=num
        
    def usoWhile(self):
        #print("Dentro de la clase",self.numero)
        # ciclo repetitivo que se ejecuta mientras la condicion se cumpla(verdadero),
        # es decir sale por falso
        caracter=""
        while caracter not in('a','e','i','o','u'):
           caracter =input("Ingrese vocal: ").lower()
           #caracter = caracter.lower()


        print("Felicitaciones el caracter: {} es una vocal".format(caracter))
    
ciclo1 = Ciclo()
#print("fuera de la clase",ciclo1.numero)  
#print(ciclo1.usoWhile())
ciclo1.usoWhile()  
        