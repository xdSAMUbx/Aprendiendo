import numpy as np

#Creando n listas de ceros
matriz_ceros = np.zeros((3,3), dtype='int8')
print(matriz_ceros)

#Creando n listas de unos
matriz_unos = np.ones((3,3),dtype='int8')
print(matriz_unos)

#---------------------- ndarrays ------------------------
list1 = np.arange(10)
list1.shape = (5,2) #El metodo shape cambia la lista segun la cantidad que queramos
print(list1[0,1])

# Como moverse a traves de los elementos de una lista método start:stop:step
list2 = np.arange(10)
print(list2[-3:3:-2]) #Si se empieza de pa tras, debe continuar para atras

