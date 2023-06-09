#creando diccionario con dict ()
diccionario = dict (nombre="Samuel",apellido="Calderon")

#las listas no pueden ser claves y se usa frozenset para meter conjuntos
diccionario = {frozenset(["Samuel","aburrido"]):"djasjds"}

#diccionario con fromkeys(), valores indefinidos
#primer dato, lo que se va a iterar, segundo dato, lo que se va a igualar
diccionario = dict.fromkeys(["nombre","apellido"])
diccionario = dict.fromkeys(["nombre","apellido"],"No se")


print(diccionario)