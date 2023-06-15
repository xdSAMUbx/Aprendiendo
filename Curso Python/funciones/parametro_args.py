#fORMA No optima
#def suma (lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados+numero
#    return numeros_sumados

#resultado = suma ([1,2,3,4,5,6,7,8,9])

#forma optima
def suma_total (numeros):
    print(numeros)
    return sum([*numeros])

resultado2 = suma_total([5,3,9,10,20,3])
print(resultado2)

#Utilizando parametro Args (*args), tiene que ser el ultimo parametro si hay mas parametros por agregar
def suma (nombre,*numeros): 
    return f"{nombre}, la suma de tus numeros es:{sum (numeros)}"

resultado = suma ("Lucas",5,3,9,10,20,3)
#print(resultado)

