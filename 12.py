# importar la clase cargo del archivo cargo.py (11)
from cargo import Cargo

class Empleado:
    secuencia=0

    def __init__(self,nom,car):
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.cargo=car
        
    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia
    def mostrar(self):
        print("({})-Nombre: {} ({})-Cargo:{} ".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion))

cargo1 = Cargo("Docente")
cargo2 = Cargo("Director")

emp1 = Empleado("Daniel",cargo1)
emp1.mostrar()
emp2 = Empleado("Daniel",cargo2)
emp2.mostrar()