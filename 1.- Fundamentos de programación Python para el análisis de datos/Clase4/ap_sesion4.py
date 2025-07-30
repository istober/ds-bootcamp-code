# Requerimiento 1
largo = int(input("Ingrese el largo del rectángulo: "))
ancho = int(input("Ingrese el ancho del rectángulo: "))

def calcular_area_rectangulo(largo, ancho):
    return largo * ancho

area_rect = calcular_area_rectangulo(largo, ancho)
print(f"El área del rectángulo es: {area_rect}")

# Requerimiento 2
from math import pi
radio = int(input("Ingrese el radio de la circunferencia: "))

def calcular_circunferencia(radio):
    return 2 * pi * radio

area_circ = calcular_circunferencia(radio)
print(f"El área de la circunferencia es: {area_circ}")

# Requerimiento 3
lista_num = [int(x) for x in input("Ingrese los números de la lista separados por una coma (,): ").split(",")]

def calcular_promedio(lista_num):
    return sum(lista_num) / len(lista_num)

promedio = calcular_promedio(lista_num)
print(f"El promedio de la lista es: {promedio}")

# Requerimiento 4
from statistics import mean

def calcular_promedio_avanzado(lista_num):
    return mean(lista_num)

promedio_avanzado = calcular_promedio_avanzado(lista_num)
print(f"El promedio avanzado de la lista es: {promedio_avanzado}")

# Requerimiento 5
import random
num_aleatorios = []
cantidad = int(input("Ingrese la cantidad de números aleatorios a generar: "))
limite = int(input("Ingrese el límite superior para los números aleatorios: "))

def generar_numeros_aleatorios(cantidad, limite):
    for _ in range(cantidad):
        numero = random.randint(1, limite)
        num_aleatorios.append(numero)
    return num_aleatorios

num_aleatorios = generar_numeros_aleatorios(cantidad, limite)
print(f"Lista de {cantidad} números entre 1 y {limite}: {num_aleatorios}")