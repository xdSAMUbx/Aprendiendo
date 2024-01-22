import pandas as pd

#funcion read_csv para leer el archivo csv
df = pd.read_csv("archivos csv\\datos.csv")
df2 = pd.read_csv("archivos csv\\datos.csv")
#names=["name","lastname","age"]
#obteniendo los datos de la columna nombre
nombres = df["nombre"]
#print(nombres)


#concepto de slicing
#cadena = "0123456789"
#con : decimos desde que posicion iniciamos y a cual terminamos, ejemplo 2:7 (slicing)
#print(cadena[2:7])

#ordenando por edad el df
df_ordenado_menor = df.sort_values("edad")
#print(df_ordenado_menor)

#ordenando de forma descendente
df_ordenado_mayor = df.sort_values("edad",ascending=False)
#print(df_ordenado_mayor)

#concatenando los dos dataframes
df_concatenado = pd.concat([df,df2])
#print(df_concatenado)

#accediendo a la primer fila con head()
primer_fila = df.head(2)
#print(primer_fila)

#accediendo a las ultimas filas
ultimas_filas = df.tail(2)
#print(ultimas_filas)

#accediendo a cantidad de filas y columnas
#filas_y_columnas_totales = df.shape
filas_totales,columnas_totales = df.shape
#filas_totales = filas_y_columnas_totales[0]
#columnas_totales = filas_y_columnas_totales[1]
#print(f"las filas son: {filas_totales}, las columnas son: {columnas_totales}")

#obteniendo data estadística del data frame
df_info = df.describe()

#accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a un elemento especifico del df con iloc
#la i hace referencia a indice
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a columnas especificas
apellidos_loc = df.loc[:,"apellido"]

#accediendo a columnas especificas
apellidos_iloc = df.iloc[:,1]

#accediendo a filas mayor a 20
mayor_que_20 = df.loc[df["edad"]>20,:]

print(mayor_que_20)

#para acceder a toda una fila o columna solo debemos usar ["para filas":"para columnas"]