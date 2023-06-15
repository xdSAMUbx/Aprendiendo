#Lambda es una funcion anonima que podemos almacenar en variables
multiplicarx2 = lambda x : x*2

#def multiplicarx2 (x):
    #return x*2

print(multiplicarx2(5))

#Beneficios:
#Retorna automaticamente
#Es sencilla
#No usar cuando hay mas de un parametro 

#Funcion que nos dice si es par:
#def es_par(num):
  #  if num%2 == 1:
 #       return True

numeros = [1,2,3,4,5,6,7,8,9]
#Usando filter con una funcion común
#numeros_pares = filter (es_par,numeros)
#print(list(numeros_pares))

#Creando pares o impares con lambda
#filter solo devuelve los elementos verdaderos
numeros_pares = filter (lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares))
