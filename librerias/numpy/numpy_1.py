import numpy as np

#Para crear listas de numpy se debe usar np.array
lista_1D = np.array([1,2,3,4]) 
lista_2D = np.array([[1,2],[2,3]])

print(f"La lista 1 es: {lista_1D}, La lista dos es: { lista_2D}")

#funciones de creación de listas en 1 dimension
# arange, permite crear listas, el numero inicial, el final y la distancia que queremos que haya entre los datos
lista3 = np.arange(0,10,1)
print(f"La lista 3 es: {lista3}")
lista4 = np.arange(2,3,.1)
print(f"La lista 4 es: {lista4}")
# linspace, permite crear listas entre un rango de números y la cantidad de elementos que deben haber detro de la lista
lista5 = np.linspace(0,10,5)
print(f"La lista 5 es: {lista5}")
lista6  = np.linspace(0,10,10, dtype="int8")
print(f"La lista 6 es: {lista6}")

#Funciones de listas 2d (matrices)
# eye, crea matrices identidad de ixj elementos
matriz1 = np.eye(2,dtype="int8")
print(f"Esta es la matriz identidad: {matriz1}")
matriz2 = np.eye(5, dtype="int8")
print(f"Esta es una matriz identidad más grande: {matriz2}")

# diag, crea matrices diagonales con valores dados, si se le ingresan 2 listas de 2d, retornara 1 lista de 1d con los valores de la diagonal
matriz3 = np.diag([1,2,3])
print(matriz3)
matriz4 = np.diag(np.arange(0,10,1, dtype="int8"))
print(matriz4)
matriz5 = np.diag([1,2,3],1) #si se le ingresa un numero, indicara el desplazamiento de la diagonal
print(matriz5)