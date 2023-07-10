#Ejercicio listas
# Escriba un programa que tenga dos lista y a continuación cree las siguientes listas
# 1 Lista de palabras que aparecen en las dos listas
# 2 Listas de palabras que aparecen en la primera lista, pero no aparecen en la segunda
# 3 Listas de palabras que aparecene en la segunda lista, pero no aparecen en la primera
# 4 Lista de palabra que aparece enambas listas

a = [1,5,79,4,6,8,53,5]
b = [1,4,53,5,5,6,3,5,]

conja = set(a)
conjb = set(b)
conjf = conja & conjb
print(f"Valores que se repiten en ambas listas: \n{conjf}")

conjf = conja - conjb

print(f"Conjuntos que apaecen en lista a pero no ne b: \n {conjf}")

conjf = conjb - conja

print(f"Conjuntos que apaecen en lista a pero no ne b: \n {conjf}")

conjf = a + b

print(f"Valores de ambas listas: \n {conjf}")

