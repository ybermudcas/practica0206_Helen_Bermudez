import os
def leer_fichero(n):
    """función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número.

    Parámetros:
        -n = el número introducido de la que se hará la tabla

    Salida:
        -Tabla de multiplicar completa
        -Si el fichero no existe muestra un mensaje por pantalla informandolo
    """
    if os.path.isfile("tabla-" + str(n) + ".txt"):
        fichero = open("tabla-" + str(n) + ".txt", "r")
        fichero_leer = fichero.read()
        print(fichero_leer)

    else:
        print("El fichero ", n, " no existe")
    
leer_fichero(5)
leer_fichero(11)