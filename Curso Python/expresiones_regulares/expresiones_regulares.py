import re

texto = '''Hola Maestro, esta es la cadena 1. como estas mi capitan
Esta es la segunda linea
y esta es la final definitiva '''

#Haciendo una busqueda simple
#resultado = re.search("Hola",texto)
#resultado = re.findall("esta",texto,flags=re.IGNORECASE)

#\d --> busca digitos númericos del 0 - 9
#resultado = re.findall(r"\d",texto)
#la r significa que usa expresiones regulares

#\D --> busca todo menos numeros
#resultado = re.findall(r"\D",texto)

#\w --> busca caracteres alfanúmericos [a-z, A-Z, 0-9, _]
#resultado = re.findall(r"\w",texto)

#\W --> busca TODO menos caracteres alfanúmericos [a-z, A-Z, 0-9, _]
#resultado = re.findall(r"\W",texto)

#\s --> busca espacios en blanco
#resultado = re.findall(r"\s",texto)

#\S --> busca TODO menos espacios en blanco
#resultado = re.findall(r"\S",texto)

#. --> Busca TODO menos saltos en linea
#resultado = re.findall(r".",texto)

#\n --> busca los saltos en linea
#resultado = re.findall(r"\n",texto)

#\ --> cancelar caracteres especiales, cancela la funcion de punto y busca puntos
#resultado = re.findall(r"\.",texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(f"\d\.\s",texto)

#^ --> busca el comienzo de una linea (buscando Hola al principio de la linea)
#re.M tiene en cuenta cada espacio de linea
#resultado = re.findall(f"^Esta",texto,flags=re.M)

#$ --> busca el final de una linea
#resultado = re.findall(r"capitan$",texto,flags=re.M)

#{n} --> Busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r"\d{1}",texto,flags=re.M)

#{n,m} --> Busca al menos n, maximo m
#resultado = re.findall(r"(ab){1,2}",texto,flags=re.M)
#usando {} encuentra al menos una coincidencia o maximo 2 coincidencias donde se encuentre el parametro
#usando antes la lista ab, encuentra todas las cadenas que tengan ab en ese orden
#usando () muestra en cantidad cuantas veces ocurre esa cadena 
#usando [] muestra la cantidad de veces que encuentra la cadena por cada lado

# | --> busca una cosa o la otra (condicion or)
resultado = re.findall(r"\d{1,4}|Hola",texto)



print(resultado)