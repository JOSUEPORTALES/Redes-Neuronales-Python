import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Grafo representado como un diccionario
# Cada nodo tiene una lista de vecinos con sus costos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('G', 2)],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []  # Nodo objetivo, no tiene vecinos
}

# Esta funcion busca el camino mas corto desde cada nodo al objetivo
# Usamos una version inversa de Dijkstra para generar la politica
def generar_politica(grafo, objetivo):
    politica = {}  # Aqui guardaremos la mejor accion desde cada nodo
    costos = {nodo: float('inf') for nodo in grafo}  # Costos iniciales infinitos
    costos[objetivo] = 0  # El costo de llegar al objetivo desde el objetivo es 0

    # Cola de prioridad para explorar nodos por menor costo
    cola = [(0, objetivo)]

    while cola:
        costo_actual, nodo = heapq.heappop(cola)

        for anterior in grafo:
            for vecino, costo in grafo[anterior]:
                if vecino == nodo:
                    nuevo_costo = costo_actual + costo
                    if nuevo_costo < costos[anterior]:
                        costos[anterior] = nuevo_costo
                        politica[anterior] = nodo  # La mejor accion es ir hacia "nodo"
                        heapq.heappush(cola, (nuevo_costo, anterior))

    return politica


# Esta funcion sigue la politica desde un nodo inicial hasta el objetivo
def seguir_politica(politica, inicio, objetivo):
    camino = [inicio]
    actual = inicio

    while actual != objetivo:
        if actual not in politica:
            return None  # No hay forma de llegar al objetivo desde este nodo
        actual = politica[actual]
        camino.append(actual)

    return camino


# Dibujamos el grafo y resaltamos un camino si se da
def dibujar_grafo(grafo, camino=None):
    G = nx.DiGraph()

    for nodo in grafo:
        for vecino, peso in grafo[nodo]:
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_weight='bold')
    etiquetas = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

    if camino:
        aristas = list(zip(camino, camino[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=aristas, edge_color='red', width=2)

    plt.title("Grafo con camino de la politica")
    plt.show()


# Definimos el nodo objetivo
nodo_objetivo = 'G'

# Generamos la politica desde todos los nodos hacia G
politica = generar_politica(grafo, nodo_objetivo)

# Imprimimos la politica generada
print("Politica generada (de cada nodo, hacia donde ir):")
for nodo in sorted(politica):
    print(f"Desde {nodo} ir a -> {politica[nodo]}")

# Simulamos seguir la politica desde un nodo inicial
nodo_inicial = 'A'
camino_resultante = seguir_politica(politica, nodo_inicial, nodo_objetivo)
print(f"\nCamino siguiendo la politica desde {nodo_inicial} hasta {nodo_objetivo}:")
print(camino_resultante)

# Dibujamos el grafo con el camino resaltado
dibujar_grafo(grafo, camino_resultante)
