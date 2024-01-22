
#with open es la manera para manetener el archivo abierto
with open("archivos\\texto.txt", encoding="UTF-8") as archivo:
    #con as le asignamos una variable
    print(archivo.read())

#con with open no es necesario cerrarlo
    