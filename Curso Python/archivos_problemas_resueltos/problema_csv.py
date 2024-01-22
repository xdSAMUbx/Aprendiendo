#cambiar dato de una columna

import pandas as pd

df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")
print(df)
#convierte los datos de una columna a string
df["edad"] = df["edad"].astype(str)

#muestra el primer elemento de la columna edad
print(type(df["edad"][0]))

#remplazando los datos "calderon" por "Nashe"
#df["apellido"].replace("calderon","Nashe",inplace=True)

#eliminando filas con datos faltantes axis se usa para determinar si se borran columnas o filas, 0 filas, 1 columnas
df = df.dropna()

#eliminando filas repetidas
df = df.drop_duplicates()

#creando un csv con el df limpio
df.to_csv("archivos_problemas_resueltos\\datos_limpios.csv")