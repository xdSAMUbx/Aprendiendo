#2 listas, una con nombres otra con apellidos
nombres = ["Samuel","Mariana","Blanca","Bibiana"]
apellidos = ["Calderon","Arango","Arevalo","Arevalo"]

#registrar esta informacion de forma optima en un txt
with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son: \n\n")
    #se usa [] para generar una lista que haga paso a paso las cosas, todo apra tenerlo en una unica linea de codigo
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------------------\n")for n,a in zip(nombres,apellidos)]