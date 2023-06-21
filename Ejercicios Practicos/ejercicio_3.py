#Ejercicio alumnos, profesores
alum_años = []
nombres = []
#Obtener nombres y edades
def edades(nombres,alum_años):
    num_alumnos = int(input("Ingrese la cantidad de alumnos que fueron a la clase: "))
    if num_alumnos == 0:
       print("Hoy no vinieron los alumnos")
    else:
        for num_alumnos in range(num_alumnos):
            nombre = input(f"Ingrese el nombre del alumno {num_alumnos}:")
            nombres.append(nombre)
            años = int(input(f"Ingrese la edad del alumno {num_alumnos}: ")) 
            alum_años.append(años)

    return nombres,alum_años

#Obtener profesor y alumno
def quien_es_quien(nombres,alum_años):
    indice_edad_maxima = alum_años.index(max(alum_años))
    profesor = nombres[indice_edad_maxima]
    print(f"El profesor es {profesor}, con {max(alum_años)} años.")
    indice_edad_minima = alum_años.index(min(alum_años))
    alumno = nombres[indice_edad_minima]
    print(f"El alumno es {alumno}, con {min(alum_años)} años.")
    
edades(nombres,alum_años)
quien_es_quien(nombres,alum_años)
            
        
            