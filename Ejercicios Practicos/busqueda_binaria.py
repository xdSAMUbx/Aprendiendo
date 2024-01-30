lista = [0,88,72,21,14,16,90,35,47,6,68,12,10,54,41]
lista.sort()

#1) Buscar el pto. medio (puntero)
#2) Comprobar si el pto. medio es el valor que buscamos
#3) si el numero es menor al valor que buscamos, aumentamos inicio 1 sobre el pto. medio (puntero)
#4) Si el numero es mayor al valor que buscamos, disminuimos el final 1 bajo el pto. medio (puntero)
#5) Si inicio se vuelve mayor o igual que final, entonces el numero no esta en la lista
print(lista)
def busqueda_binaria(valor): #devuelve el indice (posición) donde se encuentra el numero
    #el inicio siempre lleva el indice inicial del array
    inicio = 0
    #el final debe tener la cantidad total de elementos del array
    fin = len(lista) - 1
    while inicio <= fin:
        puntero = (inicio + fin) // 2
        if valor == lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            fin = puntero - 1
    return None


def buscar_valor(valor):
    res = busqueda_binaria(valor)
    if res is None:
        return f"El número {valor} no fue encontrado"
    else:
        return f"El numero {valor} se encuentra en la posicion {res}"
    
print(buscar_valor(16))