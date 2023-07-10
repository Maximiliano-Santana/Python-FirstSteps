# Tuplas son listas unmutables (Que no se pueden modificar) lo único que se puede hacer es leerla y buscar elementos las ventajs que ofrecen es que 
# son más rapidas en la ejecución y consumen menos memoria

tupla = (1,2,3)
print(tupla[2]) 

lista = list(tupla) #Transforma una tupla en una lista almacenándola en una variable (La tupla no ha sido modificada)

print(lista)

lista1 = [1,2,3,4]

tupla2 = tuple(lista1) #Transforma listas en tuplas 

print(tupla2)