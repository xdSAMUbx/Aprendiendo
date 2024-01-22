with open ("archivos\\texto.txt","w",encoding="UTF-8") as archivo:
    #escribir una linea en el archivo
    #archivo.write("Esto es una prueba y escribimos en el archivo")

    #para agregar 2 lineas
    archivo.writelines(["Hola como estas maestro\n" ,"que haces boludo?\n"])
    #\n es el enter en el texto


    #con a donde esta la w, añade cosas al archivo