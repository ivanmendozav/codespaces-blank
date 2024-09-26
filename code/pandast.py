import pandas as pd
import numpy as np
from IPython.display import display

# Parámetros para las distribuciones
n = 1  # Número de examenes
p = 0.75  # Probabilidad de éxito de pasar el examen
lambda_poisson = 1.5  # Parámetro lambda con promedio de faltas por semestre
size = 1000  # Tamaño del DataFrame
m_edad = 21 #Edad media con sd=1.8
sd_edad = 1.8

# Generar datos
binomial_data = np.random.binomial(n=n, p=p, size=size)
poisson_data = np.random.poisson(lam=lambda_poisson, size=size)
edades_data = np.floor(np.random.normal(m_edad, sd_edad, size))

# Crear DataFrame
df = pd.DataFrame({
    'Aprobacion': binomial_data,
    'Faltas': poisson_data,
    'Edad' : edades_data
})

# Mostrar las primeras filas del DataFrame
display(df.head())