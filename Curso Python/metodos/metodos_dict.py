diccionario = {
    "nombre" : "Samuel",
    "edad" : 19,
    "profesion" : "estudiante"
}

#Keys, devuelve las claves (podemos iterar)
claves = diccionario.keys()
print (claves)

#Get, obtiene el valor de la clave
#Si el valor no existe, nos devuelve none (no se encuentra)
claves_get= diccionario.get("nombre")
print(claves_get)

#pop, elimina un elemento del diccionario
diccionario.pop("nombre")
print(diccionario)

#Obtenemos un diccionario iterable (se puede recorrer)
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

#clear, elimina todo el diccionario
diccionario.clear()
print(diccionario)