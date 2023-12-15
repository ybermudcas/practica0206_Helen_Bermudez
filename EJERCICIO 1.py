def tabla_multiplicar(n):
    n = input("Escribe un número del 0 al 10")
    fichero = open("tabla-" + str(n) + ".txt", "w")
    for i in range(0, 11):
        multiplicacion = n * i
        fichero.write(str(n) + "*" + str(i) + "=" + str(multiplicacion) + '\n')
        print(n, "*", i, "=", multiplicacion)
        
#tabla_multiplicar(10)
