class Estudiante:
    def __init__(self, nombres, apellidos, codigo) -> None:
        self.nombres = nombres
        self.apellidos = apellidos
        self.codigo = codigo
        self.nota = 0
        self.faltas = 0

    # Registra nota del estudiante para la materia a la que pertenece
    def registrarNota(self, nota):
        self.nota = nota

    def registrarFaltas(self, faltas):
        self.faltas = faltas



class Paralelo:
    def __init__(self, profesor, letra) -> None:
        self.estudiantes = []
        self.letra = letra
        self.profesor = profesor

    def agregarEstudiante(self, estudiante): 
        self.estudiantes.append(estudiante)

    def PromedioNotas(self):
        return sum([estudiante.nota for estudiante in self.estudiantes])/len(self.estudiantes)

    def PromedioFaltas(self):
        return sum([estudiante.faltas for estudiante in self.estudiantes])/len(self.estudiantes)



class Escuela:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.paralelos = []

    # Agregar un paralelo a la escuela
    def agregarParalelo(self, paralelo):
        self.paralelos.append(paralelo)

    # Informa sobre los paralelos de la escuela, y el numero de alumnos matriculados
    def imprimirInforme(self):
        #Escuela: 29 de Mayo
        #Paralelo (Inscritos)   Profesor   Promedio-Notas  Promedio-Faltas 
        #A        (12 alumnos)  I.Mendoza       13.5/20           4
        #B        (10 alunos)   J.Carrion.      12.8/20           3
        print(f"Escuela: {self.nombre}")
        print(f"Paralelo (Inscritos) \t\tProfesor  \t\tPromedio Notas  \t\tPromedio Faltas")
        for paralelo in self.paralelos:
            print(f"{paralelo.letra}   ({len(paralelo.estudiantes)} alumnos)   {paralelo.profesor}   {paralelo.PromedioNotas()}   {paralelo.PromedioFaltas()} ")
