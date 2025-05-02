from collections import deque


def busqueda_en_anchura(grafo, nodo_inicial):
    visitados = set()  # Conjunto de nodos visitados
    cola = deque([nodo_inicial])  # Cola para la búsqueda en anchura

    while cola:
        nodo_actual = cola.popleft()  # Extraer el primer nodo de la cola
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            print(nodo_actual) 

            for vecino in grafo[nodo_actual]:
                if vecino not in visitados:
                    cola.append(vecino)


grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

busqueda_en_anchura(grafo, 'A')
