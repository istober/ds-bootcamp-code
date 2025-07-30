# Requerimiento 1
import numpy as np

# Requerimiento 2
vector = np.arange(1, 11)
print(vector)

# Requerimiento 3
matriz_aleatoria = np.random.rand(3, 3)
print(matriz_aleatoria)

# Requerimiento 4
matriz_identidad = np.eye(4)
print(matriz_identidad)

# Requerimiento 5
nuevo_vector = vector.reshape(2, 5)
print(nuevo_vector)

# Requerimiento 6
vector2 = vector[vector > 5]
print(vector2)

# Requerimiento 7
arreglo1 = np.arange(0, 5)
arreglo2 = np.arange(5, 10)
suma = arreglo1 + arreglo2
print(suma)

# Requerimiento 8
raiz = np.sqrt(vector)
print(raiz)
