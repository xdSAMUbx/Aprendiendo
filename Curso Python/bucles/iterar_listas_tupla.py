animales = ["perro","gato","loro","ccocodrilo"]
numeros = [10,62,12,72]

#animal es una variable que se crea para recorrer la lista
#recorriendo lista animales
for animal in animales:
    print (animal)
    
#recorriendo la lista numeros y multiplicando cada valor por 10     
for numero in numeros: 
    resultado = numero * 10
    print (f"El resultado de la variable es: {resultado}")
    
#recorriendo dos listas al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")
    
#recorriendo con range
for num in range (5,10):
    print(num)

#recorriendo una lista con su indice 
for num in enumerate(numeros):
    indice = num [0]
    valor = num [1]
    print (f'El indice es: {indice} y su valor es: {valor}') 
    
#usando el for / else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("El bucle termino")
    
#todo funciona tantro para listas como para tuplas y conjuntos