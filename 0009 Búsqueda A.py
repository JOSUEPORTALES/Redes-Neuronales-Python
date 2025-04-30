import heapq

# Nodo con estado, costo g(n), heurística h(n), y padre
class Nodo:
    def __init__(self, estado, padre=None, costo=0, heuristica=0):
        self.estado = estado
        self.padre = padre
        self.costo = costo  # g(n): costo desde el inicio hasta este nodo
        self.heuristica = heuristica  # h(n): estimación hacia el objetivo
        self.total = costo + heuristica  # f(n) = g(n) + h(n)

    # Para que se ordenen por f(n) en la cola de prioridad
    def __lt__(self, otro):
        return self.total < otro.total

# Reconstrucción del camino desde el objetivo hasta el inicio
def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo.estado)
        nodo = nodo.padre
    return list(reversed(camino))

# Algoritmo A*
def busqueda_a_estrella(inicio, objetivo, grafo, heuristicas, costos):
    frontera = []
    nodo_inicio = Nodo(inicio, None, 0, heuristicas[inicio])
    heapq.heappush(frontera, nodo_inicio)

    visitados = {}  # Guarda el menor costo g(n) conocido para cada nodo

    while frontera:
        nodo_actual = heapq.heappop(frontera)
        print(f"Explorando: {nodo_actual.estado}, g={nodo_actual.costo}, h={nodo_actual.heuristica}, f={nodo_actual.total}")

        if nodo_actual.estado == objetivo:
            return reconstruir_camino(nodo_actual)

        if nodo_actual.estado in visitados and visitados[nodo_actual.estado] <= nodo_actual.costo:
            continue  # Ya hay un camino mejor a este nodo

        visitados[nodo_actual.estado] = nodo_actual.costo

        for vecino in grafo.get(nodo_actual.estado, []):
            nuevo_costo = nodo_actual.costo + costos.get((nodo_actual.estado, vecino), 1)
            heuristica = heuristicas.get(vecino, float('inf'))
            hijo = Nodo(vecino, nodo_actual, nuevo_costo, heuristica)
            heapq.heappush(frontera, hijo)

    return None  # No se encontró camino


if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': [],
        'G': []
    }

    heuristicas = {
        'A': 6,
        'B': 4,
        'C': 4,
        'D': 6,
        'E': 2,
        'F': 4,
        'G': 0
    }

    # Costos reales entre nodos
    costos = {
        ('A', 'B'): 1,
        ('A', 'C'): 2,
        ('B', 'D'): 5,
        ('B', 'E'): 1,
        ('C', 'F'): 3,
        ('E', 'G'): 1
    }

    resultado = busqueda_a_estrella('A', 'G', grafo, heuristicas, costos)

    if resultado:
        print("\nCamino óptimo encontrado:", resultado)
    else:
        print("\nNo se encontró camino.")
