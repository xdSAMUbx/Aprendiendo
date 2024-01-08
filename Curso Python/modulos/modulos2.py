#si el modulo estuviera en una carpeta en la misma ruta
#import funciones_buenas.saludar as m_saludar

import sys

#nos devuelve las propiedades de los modulos
#print(sys.builtin_module_names)
#print(sys.path)
#nos devuelve la ruta de los modulos
sys.path.append("D:\\Programacion\\aprendiendo_python\\Curso Python\\funciones_buenas")
print(sys.path)

import saludar

print(saludar.saludar("Samuel"))