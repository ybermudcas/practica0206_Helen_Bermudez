inicial_pais = input("Introduce las iniciales del pais que quieres saber")

import os
pib = open("sdg_08_10 - sdg_08_10.tsv", "r")
leer = pib.read()
#print(leer)
separar = leer.split("\n")
print(separar)

#os.listdir("sdg_08_10 - sdg_08_10.tsv")