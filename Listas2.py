#Listas

lista=[1,2,3,4]
lista2= [9,10,11]
dias=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
combinado = ["Lunes", 2, [1,2,4], 2.5]

print(dias[2])
print(dias[0 : 2])
print(combinado)

#Funciones para listas

print(len(lista))  #Contar cantidad de elementos

lista.append(5) #Append agrega elementos al final de la lista
lista.insert(0, 0) #Inserta un elemento en la lista el primer valor es para el indice y el segundo valor es para el valor a agregar
print(lista)

lista.extend([7,8,9]) #Extiende la lista y agrega varios elementos al final de la lista
print(lista)

lista3 = lista + lista2 #Suando dos listas estas se concatenan
print(lista3)

print(3 in lista) #Verifica si el elemento se encuentra dentro de la lista, regresa un vaor booleano

print(lista.index(9)) #Retorna el indice del valor que tu pones

print(lista.count(1)) #Cuenta cuantas veces se repite un elemento

print(lista)

lista.pop() #Elimina el último elemento de la lista por default o el índice que se le indique

print(lista)

lista.remove(4) #Elimina el elemento que seindiques sin saber su posción
print(lista)

lista.clear()
print(lista)

lista4 = [1,2,3]*3 #Multiplicando por un número estas se copian esa cantidad de veces en la lista
print(lista4)
lista4.sort() #Re ordena las listas
print(lista4)
lista4.sort(reverse=True)
print(lista4)