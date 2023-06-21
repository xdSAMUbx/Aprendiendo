#asignamos el nombre que queramos al modulo
#import modulo_saludar as m_saludar 

#Desde ese modulo se importa la funcion
#from modulo_saludar import saludar

#Desde ese modulo importamos la funcion y le cambiamos el nombre
from modulo_saludar import saludar as saludo_diario

#Importar todo lo de un modulo, no recomendable
from modulo_saludar import *

saludo = saludo_diario("Samuel")
print(saludo)