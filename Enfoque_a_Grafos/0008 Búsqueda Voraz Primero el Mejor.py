import heapq  # Usamos una cola de prioridad (heap)

# Nodo con estado, padre (para reconstruir el camino) y heurística
class Nodo:
    def __init__(self, estado, padre=None, heuristica=0):
        self.estado = estado
        self.padre = padre
        self.heuristica = heuristica

    # Para que Python sepa comparar nodos en la cola de prioridad por su heurística
    def __lt__(self, otro):
        return self.heuristica < otro.heuristica

# Función para reconstruir el camino desde el nodo final hasta el inicial
def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo.estado)
        nodo = nodo.padre
    return list(reversed(camino))  # Se invierte el camino para mostrar desde el inicio

# Búsqueda Voraz Primero el Mejor
def busqueda_voraz(inicio, objetivo, grafo, heuristicas):
    # Cola de prioridad (menor heurística = mayor prioridad)
    frontera = []
    nodo_inicio = Nodo(inicio, None, heuristicas[inicio])
    heapq.heappush(frontera, nodo_inicio)

    visitados = set()  # Conjunto para no repetir nodos ya visitados

    while frontera:
        nodo_actual = heapq.heappop(frontera)
        print(f"Explorando: {nodo_actual.estado} con h={nodo_actual.heuristica}")

        if nodo_actual.estado == objetivo:
            return reconstruir_camino(nodo_actual)

        visitados.add(nodo_actual.estado)

        # Se agregan los vecinos no visitados a la frontera
        for vecino in grafo.get(nodo_actual.estado, []):
            if vecino not in visitados:
                heuristica = heuristicas.get(vecino, float('inf'))
                hijo = Nodo(vecino, nodo_actual, heuristica)
                heapq.heappush(frontera, hijo)

    return None  # Si no se encuentra el objetivo


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

    # Heurísticas estimadas (h(n)) hacia el objetivo 'G'
    heuristicas = {
        'A': 6,
        'B': 4,
        'C': 4,
        'D': 6,
        'E': 2,
        'F': 4,
        'G': 0  # El objetivo tiene h = 0
    }

    inicio = 'A'
    objetivo = 'G'

    resultado = busqueda_voraz(inicio, objetivo, grafo, heuristicas)

    if resultado:
        print("\nCamino encontrado:", resultado)
    else:
        print("\nNo se encontró un camino.")
