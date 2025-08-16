import pandas as pd

# Crear DataFrame
data = {
    'nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'edad': [25, 35, 40, 28],
    'ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Sevilla'],
    'poblacion': [3200000, 1600000, 3200000, 690000]
}

df = pd.DataFrame(data)

print("DataFrame completo:")
print(df)

# 7.5 Filtra las filas donde la ciudad sea "Madrid"
print("\nFilas donde la ciudad es 'Madrid':")
print(df[df['ciudad'] == 'Madrid'])

# 7.6 Filtra las filas donde la población sea mayor a 1,000,000
print("\nFilas donde la población es mayor a 1,000,000:")
print(df[df['poblacion'] > 1000000])