#list crea una lista / función
lista = list([15,20,10,4,19,True,False])
print(lista)

#len devuelve la cantida de elementos a la lista
resultado = len(lista)
print(resultado)

#Append, agrega elementos a la lista, no es con variables
lista.append("Nuevoelemento")
print(lista)

#Insert agrega un elemento en la lista en una posición específica
lista.insert(2,"Estamos Aprendiendo")
print(lista)

#Exten, agrega varios elementos a la lista
lista.extend([2048])
print(lista)

#Pop, elimina un elemento de la lista según su posición
#(-1) elimina el ultimo elemento de la lista, -2 para el anteultimo y así sucesivamente
lista.pop(5)
print(lista)

#Remove remueve un elemento de la lista por su valor
lista.remove("Estamos Aprendiendo")
lista.remove("Nuevoelemento")
print(lista)

#Sort, ordena de menor a mayor (solo con numeros)(primero false,true)
#Reverse, organiza al contrario (mayor a menor)
lista.sort()
print(lista)

#Reverse, invierte los elementos de una lista
lista.reverse()
print(lista)

#Clear, elimina todos los elementos de la lista
lista.clear()
print(lista)

#Para saber que puedo hacer con diferentes variables, cadenas, listas, etc...
#usar dir
#Index solo busca en listas elementos totalmente iguales