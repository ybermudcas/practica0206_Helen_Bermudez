import os
def línea_tabla(n, m):
    """Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la
      tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero.

    Parámetros:
        -n = el número introducido de la que se hará la tabla
        -m = número por el que se va a multiplicar

    Salida:
        -línea m del fichero
        -Si el fichero no existe muestra un mensaje por pantalla informandolo
    """
    if os.path.isfile("tabla-" + str(n) + ".txt"):
        fichero = open("tabla-" + str(n) + ".txt", "r")
        fichero_leer = fichero.readlines()
        print(fichero_leer[m])

    else:
        print("El fichero ", n, " no existe")

línea_tabla(5, 3)
línea_tabla(11, 4)