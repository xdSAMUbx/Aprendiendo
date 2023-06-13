numeros = [1,2,3,4,5,6,7,8,9]

#encontrando el numero mayor de una lista
numero_alto = max(numeros)
print (numero_alto)

#encontrando el numero menor de una lista
num_min = min(numeros)
print (num_min)

#redondeando a 6 decimales
numero = round(12.345678, 3)
print (numero)

#retorna false -> 0, vacio, false, ninguno, numero distinto de 0, true o cadena, datos no vacios
resultado = bool (1)
print(resultado)

#retorna true, si todos los valores son verdaderos, necesita varoles iterables (recorribles)
resultado2 = all([1,2,3,4,0])
print(resultado2)

#Retorna la suma, solo con numeros en listas,etc...
suma = sum([1,2,3,4,5])
print(suma)