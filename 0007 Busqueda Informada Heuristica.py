import heapq

# Clase para representar un nodo con heurística y referencia al padre
class Nodo:
    def __init__(self, estado, padre=None, heuristica=0):
        self.estado = estado
        self.padre = padre
        self.heuristica = heuristica

    # Esto es para que los nodos se puedan ordenar en la cola de prioridad por heurística
    def __lt__(self, otro):
        return self.heuristica < otro.heuristica

# Función para reconstruir el camino una vez se encuentra el objetivo
def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo.estado)
        nodo = nodo.padre
    return list(reversed(camino))  # Invertimos el camino para mostrar de inicio a fin

# Búsqueda informada utilizando una heurística (Greedy Best-First Search)
def busqueda_informada(inicio, objetivo, grafo, heuristicas):
    # Usamos una cola de prioridad donde los nodos con menor heurística tienen más prioridad
    frontera = []
    nodo_inicio = Nodo(inicio, None, heuristicas[inicio])
    heapq.heappush(frontera, nodo_inicio)

    visitados = set()

    while frontera:
        nodo_actual = heapq.heappop(frontera)
        print(f"Explorando: {nodo_actual.estado} con h={nodo_actual.heuristica}")

        if nodo_actual.estado == objetivo:
            return reconstruir_camino(nodo_actual)

        visitados.add(nodo_actual.estado)

        for vecino in grafo.get(nodo_actual.estado, []):
            if vecino not in visitados:
                heuristica = heuristicas.get(vecino, float('inf'))
                hijo = Nodo(vecino, nodo_actual, heuristica)
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
        'G': 0  # El objetivo tiene heurística 0
    }

    inicio = 'A'
    objetivo = 'G'

    resultado = busqueda_informada(inicio, objetivo, grafo, heuristicas)

    if resultado:
        print("\nCamino encontrado:", resultado)
    else:
        print("\nNo se encontró un camino.")
