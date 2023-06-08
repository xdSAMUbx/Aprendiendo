
cadena1="hola soy samuel"
cadena2="Bienvenidoamiprueba"

#DIR - devuelve atributos de una cadena (que se puede hacer con el dato) / funcion de python
print(dir(cadena1))

#Upper - Convierte todo a mayuscula / Metodo
resultado = cadena1.upper()
print(resultado)

#Lover - Convierte todo a minuscula / Metodo
resultado1=cadena2.lower()
print(resultado1)

#Capitalize - Primer letra en mayuscula / Metodo 
resultado2 = cadena1.capitalize()
print(resultado2)

#Find - buscar una cadena en otra cadena / metodo
#(-1) cuando no encuentra valor
busqueda_find = cadena1.find("a") 
print(busqueda_find)

#index buscamos una cadena en otra cadena / Metodo
#si no encuentra tira error o (excepcion)
busqueda_index=cadena1.index("s")
print(busqueda_index)

#si es numerico devuelve True, si no, false
es_numerico = cadena1.isnumeric()
print(es_numerico)

#si es alfanumerico devuelve true, si no, devuelve false
#no puede tener espacios, solo letras de la a hasta la z
es_alfanumerico = cadena2.isalpha()
print(es_alfanumerico)

#Count - buscar una cadena en otra cadena (devuelve cantidad de veces que se encuentra) / Metodo
busqueda_count = cadena1.count("a") 
print(busqueda_count)

#Len - contamos coincidencias de una cadena dentro de otra, devuelve la cantidad de coincidencias / funcion
contar_caracteres = len(cadena1)
print(contar_caracteres)

#verificamos si una cadena empieza con otra cadena dada, si es asi, devuelve True
empieza_con = cadena1.startswith("ho")
print(empieza_con)

#verifica con que termina una cadena dada, si termina con el parametro, devuelve True
termina_con = cadena1.endswith("0")
print(termina_con)

#remplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace("hola","holu")
print(cadena_nueva)

#split - sepada cadenas con la cadena que le pasemos 
cadena_separada = cadena1.split()
print(cadena_separada)