# Clase para crear nuevas personas
class Persona:
    def __init__(self, cedula, nombre, edad) -> None:
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.autos = []

    # Registra un nuevo auto con este dueño
    def registrar_auto(self, nuevo_auto):
        self.autos.append(nuevo_auto)

    # Calcula el total de impuestos a pagar para todos sus autos
    def calc_impuestos(self):
        total = 0
        for auto in self.autos:
            total += auto.cal_impuesto()
        return total

# Clase para crear autos dentro una instancia de persona
class Auto:
    def __init__(self, placa, marca, avaluo) -> None:
        self.placa = placa
        self.marca = marca
        self.avaluo = avaluo
    # Calcula el impuesto a pagar en base al avaluo
    # Avaluos hasta 10k pagan el 5%, otros el 10%
    def cal_impuesto(self):
        if self.avaluo <= 10000:
            return self.avaluo*0.05
        else:
            return self.avaluo*0.1

# Clase para crear cantones
class Canton:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.habitantes = []

    def registrar_habitante(self, habitante):
        self.habitantes.append(habitante)

    # Calcular impuestos de todo el canton
    def calcular_impuestos(self):
        return sum([persona.calc_impuestos() for persona in self.habitantes])