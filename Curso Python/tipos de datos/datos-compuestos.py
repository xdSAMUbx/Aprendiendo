#Lista (Modificable)
lista = ["Camilo",3,True,1.85]

#Tupla (no modificable)
tupla = ("Samuel Calderón", 3, True, 1.85) 

#Conjunto (set) (No se puede repetir valores, no se puede llamar por indice)
#print(conjunto[3]) -> No puede acceder al elemento
conjunto = {"Samuel Calderón", 3, True, 1.85}

#dict (Diccionario)
#Diccionario funciona como una lista (igual al JSON de javascript)
diccionario= {
#	Estructura del diccionario, se separa con comas
    #Clave/key		Valor/value
	"nombre" : "Samuel Calderón",
	"profesion" : "Estudiante", 
	"altura" : "1.75" 
}

print(diccionario["altura"])

