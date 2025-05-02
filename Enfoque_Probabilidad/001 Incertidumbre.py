import networkx as nx
import matplotlib.pyplot as plt
import random

# Definimos un grafo probabilistico
# Cada nodo apunta a sus vecinos con una probabilidad de transicion
grafo_probabilistico = {
    'Inicio': [('A', 0.6), ('B', 0.4)],
    'A': [('C', 0.7), ('D', 0.3)],
    'B': [('D', 1.0)],
    'C': [('Objetivo', 1.0)],
    'D': [('Objetivo', 1.0)],
    'Objetivo': []  # Nodo final sin salidas
}

# Esta funcion selecciona el siguiente nodo basado en probabilidad
def elegir_siguiente(nodo_actual):
    vecinos = grafo_probabilistico[nodo_actual]
    if not vecinos:
        return None  # Si no hay vecinos, terminamos

    nodos = [vecino for vecino, _ in vecinos]
    probabilidades = [prob for _, prob in vecinos]

    # Usamos random.choices para seleccionar segun la probabilidad
    siguiente = random.choices(nodos, weights=probabilidades, k=1)[0]
    return siguiente

# Esta funcion simula un recorrido desde un nodo inicial hasta el objetivo
def simular_camino(nodo_inicial, nodo_objetivo):
    camino = [nodo_inicial]
    actual = nodo_inicial

    while actual != nodo_objetivo:
        siguiente = elegir_siguiente(actual)
        if siguiente is None:
            break  # No hay donde ir
        camino.append(siguiente)
        actual = siguiente

    return camino

# Funcion para dibujar el grafo y mostrar el camino recorrido
def dibujar_grafo_con_camino(grafo, camino):
    G = nx.DiGraph()

    for nodo in grafo:
        for vecino, prob in grafo[nodo]:
            G.add_edge(nodo, vecino, label=f'{prob:.1f}')

    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_color='lightyellow', node_size=1500, font_weight='bold')
    etiquetas = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

    if camino:
        aristas = list(zip(camino, camino[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=aristas, edge_color='red', width=2)

    plt.title("Grafo con transiciones probabilisticas")
    plt.show()

# Ejecutamos la simulacion
camino_simulado = simular_camino('Inicio', 'Objetivo')

# Mostramos el resultado
print("Camino simulado bajo incertidumbre:")
print(" -> ".join(camino_simulado))

# Dibujamos el grafo con el camino recorrido
dibujar_grafo_con_camino(grafo_probabilistico, camino_simulado)
