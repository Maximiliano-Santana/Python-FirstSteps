# Conjutno características de los conjuntos es que dentro de ellos no puede haber otras colecciones, 
# además no pueden haber valaores duplicados y los datos son desordenados, también se pueden buscar elementos
# dentro de los conjuntos, se pueden hacer tipos de operaciones con los conjuntos, union, etc.

conjunto = set( ) #Se crea un conjunto vacío con set()

conjunto = {1,2,3,4,5,2}
 
conjunto.add(6) #Se agrega un valor nuevo al conjunto

print(conjunto)

conjunto.discard(3) #Se elimina un valor del conjunto

print(conjunto)

#Para limpiar un conjunto se puede utilizar el metodo conjunto.clear()

a = {1,2,3}
b = {3,4,5,6}

union = a | b #Union de conjuntos

print(union)

interseccion = a & b # Se crea una interseccion de ambos conjuntos

print(interseccion)

diferencia = a - b # Crea diferencia de conjuntos que que están en a pero no en b

print(diferencia)

diferenciasim = a ^ b # Crea conjunto de diferencia de conjuntos simpetrica, es decir que son número que están en a y b, pero que no están en ambos conjuntos 

print(diferenciasim)

print (a.issubset(b)) # Indica si un conjunto es subconjunto de otro, regresa booleano

print (a.issuperset(b)) # Indica si un conjunto es superconjunto de otro

print (a.isdisjoint(b)) # Conjuntos que son disconexos, que no comparten ningún elemento en común, regresa booleano

#Conjuntos inmutables, se pueden hacer inmutables con esta función a = frozenset({1,2,3,4}) crearía un conjunto inmutable