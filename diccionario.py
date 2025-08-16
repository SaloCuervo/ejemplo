animales = ["perro", "gato", "elefante", "raton", "oso"]

resultado = {}

for animal in animales:
    longitud = len(animal)  
    if longitud not in resultado:
        resultado[longitud] = []
    resultado[longitud].append(animal)

print(resultado)