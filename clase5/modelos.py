class TerrenoRectangular:
    def __init__(self, ancho, largo):
        self.ancho = ancho
        self.largo = largo

    # Metodo que retorna el area de un terreno
    def area(self):
        return self.ancho * self.largo

class TerrenoTrapezoidal:
    def __init__(self, baseMayor, baseMenor, altura):
        self.baseMayor = baseMayor
        self.baseMenor = baseMenor
        self.altura = altura

    def area(self):
        return ((self.baseMayor + self.baseMenor) / 2) * self.altura

# Modelo para una clase que contiene terrenos    
class Urbanizacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.terrenos = []

    # Permite incluir nuevos lotes a la lista de terrenos
    def  agregar_lote(self, lote):
        self.terrenos.append(lote)

    # Calcula el area total en base a los lotes que contiene
    def area_total(self):
        total = 0
        for lote in self.terrenos:
            total += lote.area() #Polimorfismo
        return total