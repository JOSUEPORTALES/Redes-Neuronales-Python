import math
import random

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, nodo1, nodo2, peso):
        if nodo1 not in self.grafo:
            self.grafo[nodo1] = []
        if nodo2 not in self.grafo:
            self.grafo[nodo2] = []
        self.grafo[nodo1].append((nodo2, peso))
        self.grafo[nodo2].append((nodo1, peso))  # Grafo no dirigido

    def obtener_vecinos(self, nodo):
        return self.grafo.get(nodo, [])

def calcular_costo(camino, grafo):
    costo = 0
    for i in range(len(camino) - 1):
        for vecino, peso in grafo.obtener_vecinos(camino[i]):
            if vecino == camino[i + 1]:
                costo += peso
                break
    return costo

def generar_vecino(camino_actual, grafo):
    # Intenta extender el camino actual con un vecino del último nodo
    ultimo_nodo = camino_actual[-1]
    vecinos = grafo.obtener_vecinos(ultimo_nodo)
    vecinos_validos = [v for v in vecinos if v[0] not in camino_actual]

    if vecinos_validos:
        nuevo_nodo, peso = random.choice(vecinos_validos)
        nuevo_camino = camino_actual + [nuevo_nodo]
        return nuevo_camino
    else:
        # Si no puede avanzar, intenta acortar el camino para explorar otra rama
        if len(camino_actual) > 1:
            return camino_actual[:-1]
        else:
            return camino_actual

def temple_simulado(grafo, inicio, objetivo, temperatura_inicial=100, enfriamiento=0.95, iteraciones=100):
    camino_actual = [inicio]
    mejor_camino = list(camino_actual)
    costo_actual = calcular_costo(camino_actual, grafo)
    mejor_costo = costo_actual
    temperatura = temperatura_inicial
    historial = []

    for i in range(iteraciones):
        nuevo_camino = generar_vecino(camino_actual, grafo)
        nuevo_costo = calcular_costo(nuevo_camino, grafo)

        delta = nuevo_costo - costo_actual

        # Aceptar la nueva solución si es mejor o con cierta probabilidad si es peor
        if delta < 0 or random.random() < math.exp(-delta / temperatura):
            camino_actual = nuevo_camino
            costo_actual = nuevo_costo

            if nuevo_camino[-1] == objetivo and (mejor_costo == 0 or nuevo_costo < mejor_costo):
                mejor_camino = nuevo_camino
                mejor_costo = nuevo_costo

        historial.append((list(camino_actual), costo_actual))
        temperatura *= enfriamiento  # Reducir la temperatura

    # Mostrar historial de caminos
    print("\nHistorial de soluciones:")
    for i, (camino, costo) in enumerate(historial):
        print(f"Iteración {i+1}: Camino: {camino} - Costo: {costo}")

    return mejor_camino, mejor_costo

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista("A", "B", 1)
grafo.agregar_arista("B", "C", 2)
grafo.agregar_arista("A", "C", 3)
grafo.agregar_arista("C", "D", 1)
grafo.agregar_arista("B", "D", 4)

# Ejecutar temple simulado
mejor_camino, mejor_costo = temple_simulado(grafo, "A", "D")
print(f"\nMejor camino encontrado: {mejor_camino} con costo: {mejor_costo}")
