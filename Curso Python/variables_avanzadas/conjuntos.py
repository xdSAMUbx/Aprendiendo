#creando conjunto con set
conjunto = set([1,2,3,4,5])

#conjunto dentro de otro conjunto

conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

print(conjunto2)

#teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando su es un subconjunto
resultado_conjuntos = conjunto2.issubset(conjunto1)
resultado_conjuntos = conjunto2 <= conjunto1

#verficando si es un superconjunto
resultado_conjuntos = conjunto2.issuperset(conjunto1)
resultado_conjuntos = conjunto2 > conjunto1

#verifica si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado_conjuntos)
