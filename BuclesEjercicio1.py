# 1 : llenar una lista con los números del 1 al 50 luego mostrar la lista con un bucle for, los elementos deben mostrarse de la siguiente forma 1-2-3-4...-50

lista = []

for i in range (1,51):
    lista.append(i)

for i in range (50):
    print(f"{lista[i]}", end = "-")
