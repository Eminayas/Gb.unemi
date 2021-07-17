class Logica:
    def __init__(self,dato): #datos poner
        self.__lista=dato        #[2,4,5]
        self.__estado=True
        
        
        
    def par(self, numero):
        # numero = int(input("Ingrese Numero: "))
        
        rec = numero % 2
        # if rec == 0:
        #     print("{} es Par".format(numero))
        # else:
        #     print("{} es Impar".format(numero))
        return rec
    
    def sumaPares(self):
        acu=0
        for num in self.__lista:
            if self.par(num) == 0:
               acu = acu + num
        return acu
                
    
    
    def divisores(self, numero):
        acu=0
        for divisor in range (1, numero):
            rec = numero % divisor
            if rec == 0:
                acu = acu + divisor
        # if acu == num:
        #     print
        return acu
    
    def divisoresNumero(self, numero):
        divisores=[]
        for divisor in range (1, numero):
            rec = numero % divisor
            if rec == 0:
                divisores.append(divisor)
        return divisores
    
                
    
    #entrada   proceso                                salida    
   #numero    obtener divisores y sumarlos
    # 6     = 1,2,3 = 6                             si es perfecto
    # 8     = 1,2,4 = 7                             no es perfecto
                 # acu=0
        # numero   divisor =1 sumandole uno    
                   
        #       6%1 = 0                          para  divisor=1 hasta numero                      
        #          +1                                    rec = numero%divisor 
        #       6%2 = 0              acu = acu+divisor    si rec = 0
        #          +1                                         acu = acu + divisor 
        #       6%4 = 0
        #          +1
        #       6%5 = 0
        #          +1
              



class Ejercicios(Logica):
    def __init__(self,numeros,valor):
       super().__init__(numeros)
       
       
    def suma(self,n1,n2):
        if super().par(n1)==0:
           return (n1+n2)*2
        else:
           return (n1+n2)
    def resta(self,n1,n2):
        return n1-n2
    
    def par(self, numero):
        rec = numero % 2
        if rec == 0:
            print(numero,"Es Par")
        else:
            print(numero,"Es Impar")
         
       
ejer = Ejercicios([2,3,4],20)
print (ejer.par(4))
print (ejer.suma(4,2))
# print(ejer.__lista)



# ejer = Logica([2,3,5,6,8])
# print(ejer.sumaPares())

        
        
# ejercicio = Logica()
# numero = int(input("Ingrese un Numero: "))
# print(ejercicio.divisoresNumero(numero))
# numeros = (6,28,3,40)
# for num in numeros:
#       if ejercicio.perfecto(num) == num:
#          print(num, "perfeto")
#       else:
#          print(num, "imperfecto")


# num = numero = int(input("Ingrese un Numero: "))
# numeros = [1,3,8,4,5,10]
# pares = []
# impares = {}
# for num in numeros: 
#     if ejercicio.par(num) == 0:  # ! se coloca para buscar impares
#         pares.append(num)
#         print(num,"par")
#     else:
#          impares[num] = "Impar"
        
# print(pares)
# print(impares)
    



       
        
               # Problema: par o impar
    # entrada   proceso                      salida
    #   numero    calculo divisible 2      par o impar
    
    # 4           4 % 2 = 0
    # 5           5 % 2 = 1
    # 8
    
    #             rec = numero%2
    #             si  rec = 0
    #                escribir "par"
    #             Sino
    #                escribir "impar"  
    # num 
    #   4     /     2 
    #   rec  (0)   2 cos 