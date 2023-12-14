n = int(input("Intruce un número entero entre 1 y 10"))
fichero = open("tabla-" + str(n) + ".txt", "w")

for i in range(0, 11):
    multiplicación = n * i
    fichero.write(str(n) + "*" + str(i) + "=" + str(multiplicación) + '\n') 
    
   # print(n, "*", i, "=", multiplicación)

