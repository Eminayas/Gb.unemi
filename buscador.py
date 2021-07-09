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
            
             
datos = [2,3,1,5,8]
#buscado=1

#datos="Hola"
#        0 1 2 3 4        
bus = Buscador(datos)
#bus.recorrerElemento()
# valor=1
# resp= bus.buscar(valor)
# if resp !=-1: print("el numero:{} se encuentra en la posicion: [{}] de la lista: {}".format(valor,resp,bus.lista))
# else: print("el numero:{} no se encuentra en la lista: {}".format(valor,bus.lista))

numerosbuscados = (2,4,6,1)
respuestas= {}
for valor in numerosbuscados:
    resp = bus.buscar(valor)
    if resp !=-1: respuestas[valor]=resp
print(respuestas)