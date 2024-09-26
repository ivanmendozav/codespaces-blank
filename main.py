import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display
import seaborn as sb

np.random.seed(4567)
df1 = pd.DataFrame(np.random.rand(20).reshape(5,4), 
                   columns=["col1","col2","col3","col4"],
                   index=["uno","dos","tres","cuatro","cinco"])

display(df1)

print(df1.loc["uno","col2"])
print(df1.iloc[0,1])

print(df1.describe())

col2 = df1.col2.to_numpy()
print(col2[0])

df2 = pd.read_csv("uploads/clase1 - 12 datos.csv")
display(df2.describe())
hombres = df2[df2.Sexo == "Masculino"]
masliviano = hombres.sort_values("Peso").iloc[0]
display(masliviano)
display(f"El hombre mas liviano es: {masliviano.name} y pesa: {masliviano.Peso}Kg.")

mujeres = df2[df2.Sexo == "Femenino"]
masliviana = mujeres.sort_values("Peso").iloc[0]
display(masliviana)
display(f"La mujer mas liviana es: {masliviana.name} y pesa: {masliviana.Peso}Kg.")