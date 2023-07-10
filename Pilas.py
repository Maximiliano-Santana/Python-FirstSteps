#Pilas entran datos y se ejecutan los que están encima o últimos que se entran es el primero en salir, no existe de forma
# explícita ne python pero se puede simular con las listas y los metodos existentes

pila = [1,2,3]

pila.append(4)
pila.append(5) # Agrega un valor al final de la lista

print (pila)

n = pila.pop() # Elimina le último elemento de la lista
print(n)

print(f"El elemento {n} ha sido elimindado de la pila") 



