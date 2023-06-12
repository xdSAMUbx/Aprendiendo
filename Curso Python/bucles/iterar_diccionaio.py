diccionario = {
    "nombre" : "Lucas",
    "apellido" : "Dalto",
    "subs" : 1000000
}

#recorriendo diccionario para obtener las claves
for key in diccionario.items():
    print(key)
    
#recorriendo diccionario con items(), con valor y key 
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es: {key}, y el valor es: {value}')
    
    