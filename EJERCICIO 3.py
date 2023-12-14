n = int(input("Escribe un número entre el 1 y 10"))
m = int(input("Escribe un número entre el 1 y 10"))

import os
if os.path.isfile("tabla-" + str(n) + ".txt"):
    fichero = open("tabla-" + str(n) + ".txt", "r")
    fichero_leer = fichero.readlines()
    print(fichero_leer[m])

else:
    print("El fichero ", n, " no existe")
