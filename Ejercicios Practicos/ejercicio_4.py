#funcionq ue verifica si el numero es primo
def es_primo (num_max):
    for i in range(2,num_max-1):
        if num_max % i == 0: return False
    return True

#funcion que nos imprime los numeros primos
def primos_hasta (num_max):
    primos = []
    for i in range (3,num_max):
        resultado = es_primo(i)
        if resultado == True : primos.append(i)
    return primos

resultado = primos_hasta(121)
print(resultado)
            