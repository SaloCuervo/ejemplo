import pandas as pd

# Crear dataframe
data = {
    'nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'edad': [25, 35, 40, 28],
    'ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Sevilla'],
    'poblacion': [3200000, 1600000, 3200000, 690000]
}

df = pd.DataFrame(data)

print("DataFrame completo:")
print(df)

#6 Indexación y selección
#6.5 Selecciona la columna "edad"
print("\nColumna 'edad':")
print(df['edad'])

#6.6 Selecciona las filas donde la edad sea mayor a 30
print("\nFilas donde la edad es mayor a 30:")
print(df[df['edad'] > 30])