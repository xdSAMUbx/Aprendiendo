#Funcion de 3 parametros
#def frase (nombre,apellido,adjetivo):
 #   return f"Hola {nombre}{apellido}, sos muy {adjetivo}"

#para organizarlo de esta forma hay que definir todos los parametros, si se define la variable queda para siempre
#frase_resultante = frase(adejtivo="capo",nombre="Samuel",apellido="Calderon")
#print(frase_resultante)

def frase (nombre,apellido,adjetivo="tonto"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

#para organizarlo de esta forma hay que definir todos los parametros, si se define la variable queda para siempre
frase_resultante = frase("samuel","Calderon","Pilo")
print(frase_resultante)