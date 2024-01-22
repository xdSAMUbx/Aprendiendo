with open ("archivos\\texto.txt","a",encoding="UTF-8") as archivo:
    #agregando lineas 
    for i in range(5):
        archivo.write(f"linea {i} agregada \n")
