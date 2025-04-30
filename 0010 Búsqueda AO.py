import heapq

# Nodo con estado, costo g(n), heurística h(n), padre y tipo (AND/OR)
class Nodo:
    def __init__(self, estado, tipo, costo=0, heuristica=0, padre=None):
        self.estado = estado
        self.tipo = tipo  # "AND" o "OR"
        self.costo = costo  # g(n): costo acumulado
        self.heuristica = heuristica  # h(n): estimación hacia el objetivo
        self.total = costo + heuristica  # f(n) = g(n) + h(n)
        self.padre = padre  # Para reconstruir el camino

    # Para ordenar los nodos por f(n)
    def __lt__(self, otro):
        return self.total < otro.total

# Reconstruir el camino desde el nodo objetivo hasta el inicial
def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo.estado)
        nodo = nodo.padre
    return list(reversed(camino))  # Invertir el camino

# Algoritmo AO* (para árboles AND-OR)
def busqueda_ao_estrella(inicio, objetivo, grafo, heuristicas):
    frontera = []
    nodo_inicio = Nodo(inicio, "OR", 0, heuristicas[inicio])
    heapq.heappush(frontera, nodo_inicio)

    visitados = set()

    while frontera:
        nodo_actual = heapq.heappop(frontera)
        print(f"Explorando: {nodo_actual.estado}, costo={nodo_actual.costo}, h={nodo_actual.heuristica}, f={nodo_actual.total}")

        # Si hemos llegado al objetivo, reconstruimos el camino
        if nodo_actual.estado == objetivo:
            return reconstruir_camino(nodo_actual)

        if nodo_actual.estado in visitados:
            continue
        visitados.add(nodo_actual.estado)

        # Expandir los nodos según el tipo (AND o OR)
        for tipo, costo, vecino in grafo.get(nodo_actual.estado, []):
            # Si es un nodo AND, sumamos el costo de todos sus caminos
            if tipo == "AND":
                costo_total = nodo_actual.costo + costo
                heuristica = heuristicas.get(vecino, float('inf'))
                hijo = Nodo(vecino, tipo, costo_total, heuristica, nodo_actual)
                heapq.heappush(frontera, hijo)
            # Si es un nodo OR, elegimos el mejor de los caminos (el de menor costo)
            elif tipo == "OR":
                costo_total = nodo_actual.costo + costo
                heuristica = heuristicas.get(vecino, float('inf'))
                hijo = Nodo(vecino, tipo, costo_total, heuristica, nodo_actual)
                heapq.heappush(frontera, hijo)

    return None  # Si no se encuentra el objetivo

# Ejemplo de uso
if __name__ == "__main__":
    grafo = {
        'A': [('OR', 0, 'B')],
        'B': [('AND', 3, 'C'), ('AND', 2, 'D')],
        'C': [('OR', 0, 'E')],
        'D': [('AND', 2, 'E')],
        'E': []  # El objetivo
    }

    heuristicas = {
        'A': 5,
        'B': 4,
        'C': 3,
        'D': 2,
        'E': 0  # El objetivo
    }

    # El objetivo es E, empezamos desde A
    resultado = busqueda_ao_estrella('A', 'E', grafo, heuristicas)

    if resultado:
        print("\nCamino óptimo encontrado:", resultado)
    else:
        print("\nNo se encontró camino.")
