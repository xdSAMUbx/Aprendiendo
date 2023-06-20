#Ejercicio alumnos, profesores

def edades():
    #pedimos la cantidad de alumnos que fueron a la clase ese dia
    num_alum = int(input("Ingrese la cantidad de alumnos que vinieron a clase hoy: "))
    list_edad = [] #iniciamos lista vacia para irla llenando 
    if num_alum == 0:
        print("El dia de hoy no vinieron alumnos")
    else:    
        for edad in range (num_alum):   
            num_años = int(input(f"La edad del estudiante {edad} es: "))
            list_edad.append(num_años) #llenamos con la edad de los alumnos que fueron a clase ese dia
    
    list_edad.sort(reverse=True)
    print(list_edad)
        
    return list_edad #retornamos la lista para que la puedan usar otras funciones si es necesario


edades()
        