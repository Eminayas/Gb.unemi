print("Sea Bienvenido")

n= input("Ingrese su nombre: \n")
e= int(input("Ingrese su edad: \n"))
drd= input ("Ingrese su direccion de domicilio: \n")
ts= input ("Ingrese su genero: \n")

print(""" Mi nombre es {} y tengo {} años. Mi genero es {}
 y la direccion de mi domicilio es {}.\n""".format(n,e,ts,drd))
 
usuario= ("El Misajo", "0701", "elmisajo@gmail.com")
materias=("Estructura de Datos", "Modelamiento de Software", "Probalidad y Estadistica", "Matematicas Discretas", "Ingles" )
docente= {"nombre":"Joe", "edad": "20", "fac": "Ing en Software"}

print(usuario, materias, docente)