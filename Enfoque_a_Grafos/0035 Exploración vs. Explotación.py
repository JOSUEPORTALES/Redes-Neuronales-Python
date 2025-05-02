import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue
import heapq

# Definimos el grafo como un diccionario
# Cada nodo tiene una lista de vecinos y el costo para llegar a ellos
grafo = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5), ('E', 3)],
    'C': [('F', 4)],
    'D': [],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Esta funcion representa la BUSQUEDA POR EXPLORACION (como BFS)
def busqueda_exploracion(inicio, objetivo):
    visitados = set()  # Conjunto de nodos ya visitados
    cola = Queue()  # Cola para mantener los caminos por explorar
    cola.put([inicio])  # Comenzamos con el nodo inicial

    while not cola.empty():
        camino = cola.get()  # Tomamos el primer camino en la cola
        nodo_actual = camino[-1]  # Vemos el ultimo nodo del camino

        if nodo_actual == objetivo:
            return camino  # Si llegamos al objetivo, devolvemos el camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino, _ in grafo.get(nodo_actual, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.put(nuevo_camino)  # Agregamos el nuevo camino a la cola

    return None  # Si no se encuentra un camino


# Esta funcion representa la BUSQUEDA POR EXPLOTACION (Greedy)
def busqueda_explotacion(inicio, objetivo, heuristica):
    visitados = set()
    cola_prioridad = []  # Usamos una cola con prioridad (heapq)

    # Agregamos el nodo inicial con su heuristica
    heapq.heappush(cola_prioridad, (heuristica[inicio], [inicio]))

    while cola_prioridad:
        _, camino = heapq.heappop(cola_prioridad)
        nodo_actual = camino[-1]

        if nodo_actual == objetivo:
            return camino

        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino, _ in grafo.get(nodo_actual, []):
                if vecino not in visitados:
                    nuevo_camino = list(camino)
                    nuevo_camino.append(vecino)
                    heapq.heappush(cola_prioridad, (heuristica[vecino], nuevo_camino))

    return None


# Heuristica estimada desde cada nodo hacia el objetivo (valor menor es mejor)
heuristica = {
    'A': 6,
    'B': 4,
    'C': 3,
    'D': 9,
    'E': 2,
    'F': 5,
    'G': 0
}

# Imprimimos los resultados de cada busqueda
camino_exploracion = busqueda_exploracion('A', 'G')
print("Camino encontrado por EXPLORACION:", camino_exploracion)

camino_explotacion = busqueda_explotacion('A', 'G', heuristica)
print("Camino encontrado por EXPLOTACION:", camino_explotacion)

# Dibujamos el grafo usando NetworkX
def dibujar_grafo(camino=None):
    G = nx.DiGraph()

    for nodo in grafo:
        for vecino, peso in grafo[nodo]:
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)

    # Dibujamos nodos y aristas
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_weight='bold')
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

    # Si hay camino, lo resaltamos en rojo
    if camino:
        aristas_camino = list(zip(camino, camino[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=aristas_camino, edge_color='red', width=2)

    plt.title("Grafo con camino resaltado")
    plt.show()

# Dibujamos el grafo con el camino de exploracion
dibujar_grafo(camino_exploracion)
