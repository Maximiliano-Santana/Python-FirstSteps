
frase = input("Escribe una frase: ")
ini = int(input("Ingrese la posición de inicio: "))
fin = int(input("Ingrese la posicioón final: "))
largo = len(frase)

for i in range (ini, fin):
    print(frase[i], end = "")
