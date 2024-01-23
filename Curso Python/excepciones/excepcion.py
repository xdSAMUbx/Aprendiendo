def sumar_dos():
    while True:
        a = input("Número 1: ")
        b = input("Número 2: ")
        try: #Se intenta el procedimiento, luego el resto
            resultado = int(a)+int(b)
        except Exception as e: #si ocurre la excepcion va a ocurrir esto
            print("Por favor, ingresa los datos correctos")
            print(f"El error es: {type(e).__name__}")
        else:
            break
        finally: #finally se ejecuta siempre en el programa
            print("Esto se ejecuta siempre")
    return resultado

print(sumar_dos())
