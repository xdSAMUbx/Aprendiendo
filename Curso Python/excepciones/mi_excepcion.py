class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste el siguiente error: {err}")

#Creando mis propias excepciones
#raise ZeroDivisionError("Que boludo, Dividiste por cero")
try:
    raise MiExcepcion("ajajajaja, persona inculta")
except:
    print("Como vas a cometer ese error?")