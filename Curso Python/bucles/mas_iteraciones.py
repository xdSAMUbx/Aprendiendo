frutas = ["Banana","manzana","Ciruela","Granadilla","Durazno","Pera"]
cadena = "Hola Samuel"
numeros = [2,4,6,8,10]

for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    
#Continuar con el bucle
for fruta in frutas:
    if fruta == "Granadilla":
        continue
    print(f"Me voy a comer una {fruta}")

#Romper el bucle
for fruta in frutas:
    if fruta == "Ciruela":
        break
    print(f"Me voy a comer una {fruta}")
    
#Recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#for para duplicar numeros
#numeros_duplicados =  list()
#for numero in numeros:
#    numeros_duplicados.append(numero*2)
    
#print(numeros_duplicados)

#for en una sola linea
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)