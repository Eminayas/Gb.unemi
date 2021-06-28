""" Construir un algoritmo tal, que dado como dato la calificación de un alumno en un examen, escriba

DEFINICIÓN DEL PROBLEMA
El mismo enunciado.

ANÁLISIS DEL PROBLEMA

Salidas: mensaje de aprobado si se cumple la condición.
Entradas: calificación
Datos adicionales:   un alumno aprueba si la calificación es mayor o igual que 7. """

class Condicion:

   def __init__(self):
       pass
       
   def NF(self):
        NT = float(input("Ingrese su Nota final:  "))
        if NT >= 7:
            print("Su nota final es {}, Felicitaciones usted ha aprobado el curso ".format(NT))   
        else:
            print("Usted ha Reprobado el Curso, con la siguiente nota {}".format(NT))
               
condi1 = Condicion() 
condi1.NF()  