import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#aprender read_csv_in_chunks para poder leer archivos con muchos datos

df = pd.read_csv("archivos_problemas_graficos\\agentes_usados.csv")
#creando el gráfico de linea
#sns.lineplot(x="agente",y="horas",data = df)

#creando grafico de barras
#sns.barplot(x="agente",y="horas",data = df)

#creando grafico de dispersion
#sns.scatterplot(x="agente",y="horas",data = df)

#grafico de bigotes
sns.boxplot(x="agente",y="horas",data = df)

#creando un punto en el momento maximo
#plt.plot("Astra",18,"o")

#obteniendo el total de horas
total_horas = df["horas"].sum()
print(f"El total de horas jugadas: {total_horas}")

#mostrar la tabla
plt.show()