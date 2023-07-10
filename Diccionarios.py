#Diccionarios

equipo = {10: "Michi", 8:"Anthony", 2:"Micha", 7:"Beta", 13:"Baieb"}

print(equipo[10]) # Muestra el índice de la clave, la clave serían los números y el indice lo que va después de os ":"

print(equipo.get(1, "No existe este jugador")) # Este método busca un jugador y si este no tiene va a mandar el mensaje entre comillas

print(10 in equipo) # Dice si la clave esta dentro del equipo

print(equipo.keys()) # Muestra solo las claves del diccionario

print(equipo.values()) # Muestra el valor de la clave

print(equipo.items()) # Muestra el dorsal y el nombre 

print(len(equipo))

equipo.clear()

print(equipo)