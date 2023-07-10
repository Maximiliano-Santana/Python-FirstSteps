# 2 Llenar una lista con los números del 1 al 10, luego modificar los elementos de la list multiplicándolos por un valor que el usuario digite

lista = [1,2,3,4,5,6,7,8,9,10]

mult = int(input("Ingrese el valor que desea multiplicar: "))

for i in range (10):
    lista [i] = mult * lista[i]

print(lista)