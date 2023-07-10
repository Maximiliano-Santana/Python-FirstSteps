# 3 Pide números y mételos en una lista, cuando el ususario meta 0 ya dejaremos de insertar, por último muestra los números ordenados de mayor a menor 
from operator import truediv

n = 1
lista=[]

while n != 0:
    n = float(input("Ingrese número: "))
    if n != 0:
        lista.append(n)

lista.sort(reverse=True)
print (lista)