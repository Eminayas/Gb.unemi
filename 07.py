""" num=10
num='20'
if type(num)==int:
    num = num*2
else:
   print('El valor no es numerico')

def mensaje(msg):
    print(msg)
   
mensaje('Bienvenido a Python')
mensaje('Mi primer Programa') """

class Sintaxis:
     #frase="instancia de la clase"
     #__int__ Metodo constructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
     # e inicializar los atributos de la clase. Self es un objeto que representa la clase creada.
    def __init__(self,dato="instancia de la clase"):
        self.frase=dato
    
    
    def usoVariables(self):
        edad, _peso = 50, 70.5
        nombres = 'Daniel Vera'
        #          012345678910
        Tipo_Sexo = 'M'
        civil = True
        #print("civil= {} y su tipo es: {}".format(civil, type(civil))) 
         # tuplas = () son colecciones de datos de cualquier tipo de inmutables
        
        usuario=()
        usuario= ('El Misajo', 701, 'elmisajo@gmail.com',True)
        #               0         1           2            3
        #usuario[4]="milagro"
        x = usuario[0]
        # listas = [] colecciones mutables
        materias=['Estructura de Datos', 'Modelamiento de Software', 'Probalidad y Estadistica', 'Matematicas Discretas', 'Ingles']
        #              0                                1                        2                          3                 4
        materias[1]="Python"
        materias.append("Go")
        # diccionario = {} colecciones de objetos clave: valor de tipo json
        docente={} #Tambien se lo puede poner vacio. 
        docente= {'nombre':'Joe', 'edad': 20, 'fac': 'Ing en Software'}
        docente["edad"]=21
        docente["cargo"]="Estudiante"
        y=docente["cargo"]
        #print(usuario,nombres[0],nombres[0:2],nombres[-1]) //  se uso para imprimir tuplas
        #print(usuario,usuario[0],usuario[0:2],usuario[-1]) //
        #print(materias, materias[2:], materias[:1], materias[::], materias[-2:]) // se uso para imprimir listas
        print(x,y)
        print(docente,docente['nombre' ]) # se lo esta usando para imprimir el diccionario
         
    def mostrar(self):
        print("mostrar")
        print(self.frase)
    
ejer1 = Sintaxis() #instancia la clase(ejecuta __init__) y se crea el objeto1 con todos los atributos y metodos de la clase Sintaxis
ejer1.usoVariables()
#print(ejer1.frase,) /// #(ejer1.edad) se agrego el ejemplo para ver que no se puede imprimir algo fuera de la clase
#ejer1.mostrar()