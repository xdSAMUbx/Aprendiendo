texto_real = input ("Por favor ingrese un texto real que diria: ")
cantidad_palabras = len(texto_real.split())
tiempo_en_decir = cantidad_palabras / 2

print(f'El tiempo que tardaria en decir toda la frase es: {tiempo_en_decir} seg')
print(f'La cantidad de palabras que dijo fue: {cantidad_palabras}')

if tiempo_en_decir > 60:
    print("Para flaco tampoco te pedi un testamento")
else:
    print('Que rapido que hablas')
    
print (f"Dalto lo diria en {cantidad_palabras *100 // 2*0.3 / 100} segundos en decirlo")