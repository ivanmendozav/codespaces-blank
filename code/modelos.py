# Importamos librerias externas
import numpy as np
import matplotlib.pyplot as plt

# Clase para calculos estadisticos
class Muestra:
    # Metodo constructor para recibir la muestra de datos
    def __init__(self, datos):
        self.datos = np.sort(datos)
    
    # Calcula la media aritmetica
    def media(self):
        return sum(self.datos) / len(self.datos)
    
    # Calcula la mediana de la muestra (valor medio)
    def mediana(self):
        n = len(self.datos)
        pos = (n+1)/2
        if n % 2 != 0:
            return self.datos[int(pos-1)]
        else:
            return (self.datos[int(pos-1)] + self.datos[int(pos)])/2
        
    # Retorna el tamaño de la muestra
    def size(self):
        return len(self.datos)
    
    # Plotea un histograma con pyplot
    def histograma(self, b=5):
        plt.hist(self.datos, bins=b)
        plt.grid()
        plt.show()

    # Cuartil 
    def cuartil(self, k):
        return np.quantile(self.datos, k/4)
