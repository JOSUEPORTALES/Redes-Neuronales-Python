# Importamos la función para calcular distancia entre vectores
from math import sqrt

# Lista de ejemplos (entrenamiento)
# Cada elemento tiene la forma: [color_rojo, color_amarillo], tipo_de_fruta
# color_rojo y color_amarillo son 1 si el color está presente, 0 si no
datos_entrenamiento = [
    ([1, 0], "manzana"),    # Manzana es roja
    ([0, 1], "platano"),    # Plátano es amarillo
    ([1, 1], "manzana"),    # Algunas manzanas pueden ser rojo-amarillas
    ([0, 1], "platano")
]

# Función para calcular la distancia euclidiana entre dos vectores
def distancia_euclidiana(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Función para clasificar una nueva fruta
def clasificar_fruta(nueva_fruta):
    distancia_minima = float('inf')   # Iniciamos con una distancia infinita
    tipo_predicho = None              # Aquí guardaremos la fruta predicha

    # Recorremos cada ejemplo de entrenamiento
    for ejemplo in datos_entrenamiento:
        caracteristicas, tipo = ejemplo
        distancia = distancia_euclidiana(nueva_fruta, caracteristicas)
        
        # Si la distancia es menor a la mínima encontrada, actualizamos
        if distancia < distancia_minima:
            distancia_minima = distancia
            tipo_predicho = tipo

    return tipo_predicho

# Nueva fruta a clasificar (solo contiene el color amarillo)
nueva_fruta = [0, 1]

# Ejecutamos la clasificación
fruta_clasificada = clasificar_fruta(nueva_fruta)

# Mostramos el resultado
print("La nueva fruta es clasificada como:", fruta_clasificada)
