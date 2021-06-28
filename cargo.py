class Cargo: # necesito una estructura y modelo por esa razon se crea la clase cargo ya defino la estructura para futuros usos.
    secuencia=0 # no necesita estar instanciado asi que no se necesita crear un objeto.
    def __init__(self,des="Sin Cargo"): # parametros
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia # SOLO SON VALORES DE LA INSTANCIA
        self.descripcion=des # self trabaja internamente dentro de la clase
        
if __name__ == "__main__":
       
 cargo1 = Cargo("Docente") #instacia la clase y crea un objeto / ejecuta el constructor. // () si no se coloca nada, procede a dar un error porque le falta un parametro que presentar.
 #print("Cargo 1",cargo1.secuencia)
 print(cargo1.codigo,cargo1.descripcion)

 cargo2 = Cargo("Analista")
 #print("Cargo 2",cargo2.secuencia)
 print(cargo2.codigo,cargo2.descripcion)

 cargo3 = Cargo("Conserje")
 #print("Cargo 3",cargo3.secuencia)
 print(cargo3.codigo,cargo3.descripcion)
 # print(Cargo.secuencia) ejemplo
 print(Cargo.secuencia)
 print(cargo1.secuencia)
 print(cargo2.secuencia)
 print(cargo3.secuencia)


