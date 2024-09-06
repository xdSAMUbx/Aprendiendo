import os
# Libreria OS; para poder dar manejo a las carpetas del computados
print(os.path) #donde se encuentran las librerias que nos ofrece
print(os.getcwd()) #cwd = Current Working Directory; por lo tanto nos muestra el directorio actual desde el cual estamos trabajando
print(os.name) #imprime el sistema como lo conocemos de una forma  más discreta
#os.chdir("..") # Change Directory; cambia el directorio en el cual nos encontramos
print(os.listdir()) # Nos indica los elementos que hay en nuestro directorio
#os.mkdir("nuevo_directorio")
#os.chdir("nuevo_directorio")


import sys
#Libreria SYS; poder enlazar el programa con el sistema operativo
print(sys.platform) #imprime el sistema como lo conocemos
print("Saliendo del prorama ...")
#sys.exit() # Finaliza el programa 
print(sys.getwindowsversion()) #Nos muestra la version de windows en la cual nos encontramos
#print(sys.modules) #Nos muestra los modulos cargados en python
print(sys.version)
print(sys.version_info)


import platform

print(platform.architecture())
print(platform.machine())
print(platform.processor())
print(platform.platform())
print(platform.system())
print(platform.uname())