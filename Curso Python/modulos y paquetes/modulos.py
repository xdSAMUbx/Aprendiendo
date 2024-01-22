#asignamos el nombre que queramos al modulo
import modulo_saludar as m_saludar 

#Desde ese modulo se importa la funcion
#from modulo_saludar import saludar

#Desde ese modulo importamos la funcion y le cambiamos el nombre
#from modulo_saludar import saludar as saludo_diario

#Importar todo lo de un modulo, no recomendable
#from modulo_saludar import *

saludo = m_saludar.saludar("Samuel")
print(saludo)

#propiedades y metodos del namespace
#print(dir(m_saludar))

#muestra el nombre del modulo que se importa
#print(m_saludar.__name__)

#el modulo que se ejecuta es este mismo (principal / main)
print(__name__)