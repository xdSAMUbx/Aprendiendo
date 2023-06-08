ingreso_mensual = 12000
gasto_mensual = 2000

#elif e if anidados

if ingreso_mensual >10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien en cualquier parte del mundo")
    else:
        print("Estas gastando mucho")
    
elif ingreso_mensual >1000:
    print ("Estas bien en latam")
    
#Se puede poner cuantos elif quiera   

else:
    print ("Eres pobre")