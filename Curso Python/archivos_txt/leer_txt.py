archivo_sin_leer = open("archivos\\texto.txt",encoding ="UTF-8")

#funcion .read nos permite ver que hay dentro del txt
#archivo = archivo_sin_leer.read()
#print(archivo)

#para leer linea por linea
#lineas = archivo_sin_leer.readlines()
#print(lineas)

#leer una sola linea
#.readline(# de caracteres a leer)
linea = archivo_sin_leer.readline()
print(linea)

#si se quiere leer una cantidad grande de texto, usar otras maneras para leer archivos

#cerrar el archivo
archivo_sin_leer.close()