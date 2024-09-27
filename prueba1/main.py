# librerias
from modelos import Escuela,Estudiante,Paralelo
import numpy as np

# Paralelo A
## Estudiantes
codigo = np.random.randint(10000,20001,1)
andres = Estudiante("Andres","Lopez H",codigo)
andres.registrarFaltas(3)
andres.registrarNota(10.5)

codigo = np.random.randint(10000,20001,1)
victor = Estudiante("Victor","Valverde H",codigo)
victor.registrarFaltas(3)
victor.registrarNota(15.1)

paraleloA = Paralelo("I. Mendoza","A")
paraleloA.agregarEstudiante(andres)
paraleloA.agregarEstudiante(victor)

# Paralelo B
## Estudiantes
codigo = np.random.randint(10000,20001,1)
miguel = Estudiante("Miguel","Jimenez T",codigo)
miguel.registrarFaltas(2)
miguel.registrarNota(15)

codigo = np.random.randint(10000,20001,1)
sandra = Estudiante("Sandra","Gonzalez A",codigo)
sandra.registrarFaltas(1)
sandra.registrarNota(11)


paraleloB = Paralelo("J. Carrion","B")
paraleloB.agregarEstudiante(miguel)
paraleloB.agregarEstudiante(sandra)

# Escuela
mi_escuela = Escuela("29 de Mayo")
mi_escuela.agregarParalelo(paraleloA)
mi_escuela.agregarParalelo(paraleloB)

# Mis informes
## A nivel de escuela
print("\n\nINFORME DE ESCUELA:")
mi_escuela.imprimirInforme()
