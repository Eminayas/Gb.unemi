class Buscador:
    def __init__(self,dato):
        self.lista=dato
        
        
    def recorrerElemento(self):
        for ele in self.lista:   #[::-1] / para colocarlo al reves 
            print(ele,end=" ")
        for ele in self.lista[::-1]:
            print(ele,end=" ")    
            
        print()     
        for pos,ele in enumerate(self.lista):
            print("[{}]={}  ".format(pos,ele))
        print()    
        
        for pos in range(len(self.lista)-1,0,-1):
            print("[{}]={}  ".format(pos,self.lista[pos]))     
    
    
    def buscar(self,buscado):
        encontrado=False
        for pos,ele in enumerate(self.lista):
             if ele==buscado:
                 encontrado=True
                 break # rompe el for
                 
         
        if encontrado:   return pos
        else:            return -1 
        
    def ordenarAsc(self):
        for pos in range(0,len(self.lista)-1):
            for sig in range(pos+1, len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux
        
    def ordenarDes(self):
        for pos in range(0,len(self.lista)-1):
            for sig in range(pos+1, len(self.lista)):
                if self.lista[pos] < self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux           
            
             
             
     
    def primer(self):
        return self.lista[0]
    
    def primerElemento(self):
        primero=self.lista[0]
        self.lista = self.lista[1:]
        return primero
    
    def primerElemento2(self):
        primero=self.lista[0]
        auxiliar=[]
        for pos in range(1, len(self.lista)):
            auxiliar.append(self.lista[pos])
        self.lista=auxiliar
        return primero     
    
    
    def ultimo(self):
        return self.lista[-1]
    
    def ultimoElemento(self):
        ultimo=self.lista[-1]
        self.lista = self.lista[:-1]
        return ultimo  

    def ultimoElemento2(self):
        ultimo=self.lista[-1]
        auxiliar=[]
        for pos in range(0,len(self.lista)-1):
            auxiliar.append(self.lista[pos])
        self.lista=auxiliar
        return ultimo
          
          
          
    def insertar(self,num):
        self.ordenarAsc()
        auxiliar=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                auxiliar.append(num)
                break
        
        self.lista=self.lista[0:pos]+auxiliar+self.lista[pos:]
        
        
    def insertar2(self,num):
        self.ordenarAsc()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if num < ele:
                break
        for i in range(pos):
            auxlista.append(self.lista[i])
        auxlista.append(num)
        for j in range(pos,len(self.lista)):
            auxlista.append(self.lista[j])
        self.lista=auxlista
            
        # self.lista=self.lista[0:pos]+auxiliar+self.lista[pos:]
          
          
          
    def insertarOrden(self,num):
        self.lista.append(num)
        self.ordenarAsc()
          
   
    def eliminar(self,num):
        enc=False
        for pos,ele in enumerate(self.lista):
            if num == ele:  
                enc=True
                break
        if enc: self.lista=self.lista[0:pos]+self.lista[pos+1:]
        return enc    
             
             
             
             
             
             
datos = [2,3,8,10] #= [2,3,5,8,10]   #Ejecutar

# # insertar = 5 = [2,3,8,10]

#bus = Buscador(datos)
# # num=18
#datos.sort()          # haciendo pruebas con el sort ascendentes / sorted
#print(datos)          # para que me imprima las lista ordenada
#bus = Buscador(datos)                                                                                       #Ejecutar

# if bus.eliminar(2)==True: print("El numero que coloco se elimino de la lista", bus.lista)                   #Ejecutar
# else: print("El numero agregado no se encuentra en la lista, por ese motivo no se procede a eliminar")      #Ejecutar

# print(bus.ultimoElemento2(),bus.lista)                                                                      #Ejecutar





#print(datos)
# bus = Buscador(datos)
# print(bus.lista)
# bus.ordenarAsc()
# print(bus.lista)
# bus.ordenarDes()
# print(bus.lista)



#buscado=1

#datos="Hola"
#        0 1 2 3 4        

#bus.recorrerElemento()
# valor=1
# resp= bus.buscar(valor)
# if resp !=-1: print("el numero:{} se encuentra en la posicion: [{}] de la lista: {}".format(valor,resp,bus.lista))
# else: print("el numero:{} no se encuentra en la lista: {}".format(valor,bus.lista))

# numerosbuscados = (2,4,6,1)
# respuestas= {}
# for valor in numerosbuscados:
#     resp = bus.buscar(valor)
#     if resp !=-1: respuestas[valor]=resp
# print(respuestas)


                                                           
                                            
                                            #Ejemplo 



# lista = [2,4,8,5,10,7,8,9]
# #        0 1 2 3 4  5 6 7

# x = lista[2]
# lista1 = lista[1:]
# lista2 = lista[1:3]
# lista3 = lista[0:-1]
# lista4 = lista[+1]
# lista5 = lista[1:-1]
# lista6 = lista[:-1]

# for pos in range(len(lista)-1):
#     print("Primer for",pos,lista[pos])
#     for j in  range(pos+1,len(lista)):
#         print("Segundo for",lista[j])
#     input("presione alguna tecla para continuar....")