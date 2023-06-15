#creando una funcion simple
#def saludar ():
    #print("Hola Samuel, como vas?")
#ejecutando la funcion simple
#saludar()

#Funcion con parametro (nombre es el parametro)
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if sexo == "mujer":
        adjetivo = "Reina"
    elif sexo == "hombre":
        adjetivo = "titan"
    else: 
        adjetivo = "amor"
          
    print(f"Hola {nombre}, mi {adjetivo} ¿Como vas?")
    
saludar ("Mariana","Mujer")
saludar ("Samuel","hOMBRE")
saludar ("Camilo","bISExual")

#crear una funcion que nos retorne valores
def crear_contraseña_random (num):
    chars = "abcdefghij"
    num_int = str(num)
    num = int (num_int[0])
    c1 = num - 2
    c2= num
    c3= num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    #print (contraseña), devolveria None en el print(frase), pues no se retorna valor
    return contraseña,num 
    #Es un valor que le podemos asignar a una variable, si hay una variable global llamada contraseña
    #o a una variable x le asignamos contraseña se va a actrualizar cada vez que se use la funcion
    
    #se pueden devolver multiple valores armando tuplas, puesto que no puden modificarse
    
#usando el desempaquetado
password,numero_usado = crear_contraseña_random(98)
print(f"Tu contaseña es: {password}")
print(f"El numero usado fue:{numero_usado}")
