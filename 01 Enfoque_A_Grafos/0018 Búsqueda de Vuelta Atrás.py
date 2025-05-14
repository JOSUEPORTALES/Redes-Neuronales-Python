import networkx as nx
# La biblioteca NetworkX (nx) se utiliza para la creación, manipulación y visualización de grafos y redes.
# Proporciona herramientas para trabajar con grafos dirigidos, no dirigidos, ponderados, entre otros.


# Importamos las bibliotecas necesarias
import matplotlib.pyplot as plt

# Definimos una función para realizar la búsqueda de vuelta atrás (backtracking)
def busqueda_vuelta_atras(grafo, nodo_inicio, nodo_objetivo, camino=[]):
    """
    Función que implementa la búsqueda de vuelta atrás en un grafo.
    :param grafo: Diccionario que representa el grafo.
    :param nodo_inicio: Nodo desde donde comenzamos la búsqueda.
    :param nodo_objetivo: Nodo que queremos encontrar.
    :param camino: Lista que almacena el camino actual.
    :return: Lista con el camino encontrado o None si no hay solución.
    """
    camino = camino + [nodo_inicio]  # Agregamos el nodo actual al camino
    if nodo_inicio == nodo_objetivo:  # Si encontramos el nodo objetivo, devolvemos el camino
        return camino
    if nodo_inicio not in grafo:  # Si el nodo no tiene conexiones, devolvemos None
        return None
    for vecino in grafo[nodo_inicio]:  # Iteramos sobre los nodos vecinos
        if vecino not in camino:  # Evitamos ciclos revisando si el vecino ya está en el camino
            nuevo_camino = busqueda_vuelta_atras(grafo, vecino, nodo_objetivo, camino)
            if nuevo_camino:  # Si encontramos un camino válido, lo devolvemos
                return nuevo_camino
    return None  # Si no encontramos solución, devolvemos None

# Creamos un grafo de ejemplo como un diccionario
grafo = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# Definimos el nodo de inicio y el nodo objetivo
nodo_inicio = "A"
nodo_objetivo = "F"

# Llamamos a la función de búsqueda de vuelta atrás
camino_encontrado = busqueda_vuelta_atras(grafo, nodo_inicio, nodo_objetivo)

# Imprimimos el resultado
print("Camino encontrado:", camino_encontrado)

# Visualizamos el grafo y el camino encontrado
G = nx.DiGraph()  # Creamos un grafo dirigido
for nodo, vecinos in grafo.items():
    for vecino in vecinos:
        G.add_edge(nodo, vecino)  # Agregamos las aristas al grafo

# Dibujamos el grafo
pos = nx.spring_layout(G)  # Calculamos la posición de los nodos
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=15)

# Si encontramos un camino, resaltamos las aristas del camino
if camino_encontrado:
    aristas_camino = [(camino_encontrado[i], camino_encontrado[i+1]) for i in range(len(camino_encontrado)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=aristas_camino, edge_color="red", width=2)

# Mostramos el grafo
plt.title("Grafo con el camino encontrado")
plt.show()