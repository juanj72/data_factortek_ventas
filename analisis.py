import pandas as pd


datos = pd.read_csv('cab.csv')
datos = pd.DataFrame(datos)


#print(datos)

print(datos.describe())

