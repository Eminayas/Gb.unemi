class Condicion:

   def __init__(self,num1,num2): #va a ejecutar el metodo constructor
       self.numero1=num1         #tiene variables locales
       self.numero2=num2         #variable self especiales / variables de instancia de la clase
       numero = self.numero1+self.numero2
       self.numero3=numero
       
   def Condicion(self):
        #if ... elif... else...: permiten condicionar la ejecucion de uno o varios bloques  
        # de sentencias al cumplimiento de una o varias condiciones.  
        if self.numero1 == self.numero2:
              print("numero1: {} y numero2: {} son iguales".format(self.numero1,self.numero2))   
        elif self.numero1 < self.numero3:
              print("numero1: {} es menor numero3: {}".format(self.numero1,self.numero3))
        else:
            print("no son iguales")
        print("fin del metodo")
               
condi1 = Condicion(8,18)  #variables 'numero' son creadas fuera de la clase
print(condi1.numero3) 
print(condi1.Condicion())      


