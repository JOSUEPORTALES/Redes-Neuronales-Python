import random
"""
Este programa implementa un algoritmo genético para encontrar el camino más corto entre dos nodos en un grafo no dirigido.
El algoritmo utiliza una población inicial de caminos generados aleatoriamente y aplica operaciones de selección, cruzamiento
y mutación para evolucionar hacia una solución óptima.
Clases:
    - Grafo: Representa un grafo no dirigido con métodos para agregar aristas y obtener vecinos de un nodo.
Funciones:
    - calcular_costo(camino, grafo): Calcula el costo total de un camino en el grafo.
    - generar_camino(grafo, inicio, objetivo, max_longitud): Genera un camino aleatorio desde un nodo inicial hasta un nodo objetivo.
    - cruzar(padre1, padre2): Realiza el cruzamiento entre dos caminos para generar un nuevo camino.
    - mutar(camino, grafo, prob_mutacion): Aplica una mutación a un camino con una probabilidad dada.
    - algoritmo_genetico(grafo, inicio, objetivo, poblacion_size, generaciones): Implementa el algoritmo genético para encontrar el camino más corto.
Uso:
    1. Crear un grafo utilizando la clase `Grafo` y agregar aristas con pesos.
    2. Llamar a la función `algoritmo_genetico` especificando el grafo, el nodo inicial, el nodo objetivo, el tamaño de la población y el número de generaciones.
    3. El programa imprimirá el historial de soluciones y el mejor camino encontrado junto con su costo.
Ejemplo:
    print(f"Mejor camino encontrado: {mejor_camino} con costo: {mejor_costo}")
"""



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
    return costo if len(camino) > 1 else float('inf')

def generar_camino(grafo, inicio, objetivo, max_longitud=10):
    camino = [inicio]
    actual = inicio
    while actual != objetivo and len(camino) < max_longitud:
        vecinos = [v for v, _ in grafo.obtener_vecinos(actual) if v not in camino]
        if not vecinos:
            break
        siguiente = random.choice(vecinos)
        camino.append(siguiente)
        actual = siguiente
    return camino

def cruzar(padre1, padre2):
    interseccion = list(set(padre1) & set(padre2))
    if not interseccion or interseccion[0] == padre1[0]:
        return padre1
    punto = interseccion[0]
    i1 = padre1.index(punto)
    i2 = padre2.index(punto)
    hijo = padre1[:i1] + padre2[i2:]
    return hijo

def mutar(camino, grafo, prob_mutacion=0.3):
    if len(camino) < 2 or random.random() > prob_mutacion:
        return camino
    idx = random.randint(0, len(camino) - 2)
    nodo = camino[idx]
    vecinos = [v for v, _ in grafo.obtener_vecinos(nodo) if v not in camino]
    if vecinos:
        nuevo_nodo = random.choice(vecinos)
        return camino[:idx+1] + [nuevo_nodo]
    return camino

def algoritmo_genetico(grafo, inicio, objetivo, poblacion_size=10, generaciones=30):
    poblacion = [generar_camino(grafo, inicio, objetivo) for _ in range(poblacion_size)]
    historial = []

    for gen in range(generaciones):
        # Calcular costos
        poblacion = [(camino, calcular_costo(camino, grafo)) for camino in poblacion]
        poblacion.sort(key=lambda x: x[1])  # Menor costo primero

        # Guardar historial
        for camino, costo in poblacion[:3]:  # Solo los mejores 3
            historial.append((list(camino), costo))

        # Ver si ya llegamos al objetivo
        for camino, costo in poblacion:
            if camino[-1] == objetivo:
                print("\nHistorial de soluciones:")
                for i, (cam, cost) in enumerate(historial):
                    print(f"Generación {i+1}: Camino: {cam} - Costo: {cost}")
                return camino, costo

        # Selección: los mejores sobreviven
        seleccionados = [camino for camino, _ in poblacion[:poblacion_size // 2]]

        # Cruzamiento y mutación para nueva generación
        nueva_poblacion = []
        while len(nueva_poblacion) < poblacion_size:
            padre1 = random.choice(seleccionados)
            padre2 = random.choice(seleccionados)
            hijo = cruzar(padre1, padre2)
            hijo = mutar(hijo, grafo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    print("\nHistorial de soluciones:")
    for i, (cam, cost) in enumerate(historial):
        print(f"Generación {i+1}: Camino: {cam} - Costo: {cost}")
    return None, None

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_arista("A", "B", 1)
grafo.agregar_arista("B", "C", 2)
grafo.agregar_arista("A", "C", 3)
grafo.agregar_arista("C", "D", 1)
grafo.agregar_arista("B", "D", 4)

# Ejecutar Algoritmo Genético
mejor_camino, mejor_costo = algoritmo_genetico(grafo, "A", "D")

if mejor_camino:
    print(f"\nMejor camino encontrado: {mejor_camino} con costo: {mejor_costo}")
else:
    print("\nNo se encontró un camino válido.")
