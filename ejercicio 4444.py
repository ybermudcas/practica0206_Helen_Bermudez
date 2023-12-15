import urllib.request

acceder_texto = urllib.request.urlopen("http://textfiles.com/adventure/aencounter.txt")
leer = acceder_texto.read()
#print(leer)
separar = leer.split()
#print(separar)
print(len(separar))
