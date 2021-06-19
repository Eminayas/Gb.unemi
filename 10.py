class For:
    def __init__(self,lim=12):
        self.n=lim
    
    def usoFor(self):
        # ciclo repetitivo automatico (de incrementos o decrementos) que se ejecuta hasta alcanzar (el valor final) un valor final.
       nombre = "Daniel"
       #pos      012345
       datos=["Daniel",50,True]
       #pos     0       1   2 
       numeros=(2,5,6,4,1)
       docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
       listaNotas = [(30,40), (20,40,50),(50,40)]
       listaAlumnos = [{"nombre":"Erick","final":70}, {"nombre":"Yadi","final":60},{"nombre":"Danny","final":90}]
        # range([inicio=0], limite, [inc/dec=0]). Generea un rango de valores desde un valor inicial a un valor final
        # for con range() para generar valores o for con colecciones para recorrer elementos por elementos de la coleecione
        #for i in range(5): #genera valores (0,1,2,3,4)
        #     print("i={}".format(i))
        #for i in range(2,5): #genera valores (2,3,4)
        #    print("i={}".format(i))
        #for i in range(3,self.n,3): #genera valores (3,6,9)
        #    print("i={}".format(i), end=" ")
        #    long = len(nombre)
        #    for pos in range(long): #(0,1,2,3,4,5)
        #        print(nombre[pos],end= " ")
        #    long = len(datos)
        #    for pos in range(long): #(0,1,2,3,4,5)
        #        print(datos[pos],end= " ")
        #    for pos,elem in enumerate(nombre): #((0,"daniel"),(1,50),(2,true))
        #        print(pos," ",elem)
        #    for elem in datos: # 'danuiel'.50,true
        #        print(elem)
        #    for num in numeros: print(num)
        #    daniel
        #    012345
        #    for pos,elem in enumerate(nombre): #
        #        if pos%2==0 and pos!=0:
        #           print(elem)
        #    docente = {'nombre': 'Daniel', 'edad': 50, 'fac': 'faci'}
        #    for clave,valor in docente.items():
        #        print(clave,valor, end=" ")
        #    lista = [2,4,5,5]
        #    acu=0
        #    for ele in lista:
        #         acu=acu+ele
        #    print(acu)
        #    acu=0
        #    listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yadi","final":60},{"nombre":"Danny","final":90}]   
        #    for alumnos in listaAlumnos:
        #        print(alumnos)
        #        acu=acu + alumnos["final"]
        #    print(acu)
        #    acu=0
        #    cont=0
        #    listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yadi","final":60},{"nombre":"Danny","final":90}]   
        #    for alumnos in listaAlumnos:
        #        cont+=1
        #        for c,v  in alumnos.items():
        #           print(c,v)
        #           if c=="final":
        #              acu = acu+v
        #    #print(acu,acu/len(listaAlumnos))
        #    print(acu,acu/cont)
       
       listaNotas = [(30,40),(20,40,50),(50,40,10,45),(5,15)]
       acu,cont=0,0
       for notas in listaNotas:
           print(notas)
           acumParcial=0
           for nota in notas:
               #print(nota)
               #acu+=nota
               acumParcial+=nota
               #cont+=1
           cont+= len(notas)
           acu+= acumParcial
           print(acumParcial,acumParcial/len(notas))
       print(acu,acu/cont)
       
bucle1 = For()
bucle1.usoFor()

# bucle2 = For(12)
# bucle2.usoFor() 
#print(bucle.numero)

