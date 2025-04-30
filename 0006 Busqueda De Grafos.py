from collections import deque

# Clase para representar un nodo con su estado y su padre (para reconstruir el camino)
class Nodo:
    def __init__(self, estado, padre=None):
        self.estado = estado
        self.padre = padre

# Función para reconstruir el camino desde el nodo inicial hasta el objetivo
def reconstruir_camino(nodo):
    camino = []
    while nodo:
        camino.append(nodo.estado)
        nodo = nodo.padre
    return list(reversed(camino))  # Invertimos el camino para mostrar de inicio a objetivo

# Búsqueda en grafos usando búsqueda en amplitud (BFS)
def busqueda_en_grafos(inicio, objetivo, grafo):
    # Cola para mantener los nodos por explorar
    frontera = deque()
    nodo_inicio = Nodo(inicio)
    frontera.append(nodo_inicio)

    # Conjunto de nodos ya visitados para evitar repeticiones
    visitados = set()
    visitados.add(inicio)

    while frontera:
        nodo_actual = frontera.popleft()
        print(f"Visitando: {nodo_actual.estado}")

        if nodo_actual.estado == objetivo:
            return reconstruir_camino(nodo_actual)

        # Se expanden los vecinos del nodo actual
        for vecino in grafo.get(nodo_actual.estado, []):
            if vecino not in visitados:
                visitados.add(vecino)  # Marcamos como visitado
                hijo = Nodo(vecino, nodo_actual)
                frontera.append(hijo)

    return None  # Si no se encuentra un camino

# Ejemplo de uso
if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'G'],
        'F': ['C'],
        'G': ['E']
    }

    inicio = 'A'
    objetivo = 'G'

    resultado = busqueda_en_grafos(inicio, objetivo, grafo)

    if resultado:
        print("Camino encontrado:", resultado)
    else:
        print("No se encontró un camino.")
