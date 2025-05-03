# Importamos las bibliotecas necesarias
import networkx as nx  # Para trabajar con grafos
import matplotlib.pyplot as plt  # Para graficar los grafos

# Definimos una función para realizar la propagación de restricciones en un grafo
def propagacion_restricciones(grafo, restricciones):
    """
    Esta función aplica restricciones a un grafo y elimina nodos o aristas
    que no cumplen con las restricciones dadas.
    """
    # Creamos una copia del grafo para no modificar el original
    grafo_filtrado = grafo.copy()

    # Iteramos sobre las restricciones
    for nodo, restriccion in restricciones.items():
        # Si el nodo está en el grafo
        if nodo in grafo_filtrado:
            # Obtenemos los vecinos del nodo
            vecinos = list(grafo_filtrado.neighbors(nodo))
            # Aplicamos la restricción eliminando vecinos que no cumplen
            for vecino in vecinos:
                if vecino not in restriccion:
                    grafo_filtrado.remove_edge(nodo, vecino)  # Eliminamos la arista

    return grafo_filtrado

# Creamos un grafo de ejemplo
grafo = nx.Graph()

# Agregamos nodos al grafo
grafo.add_nodes_from(["A", "B", "C", "D", "E"])

# Agregamos aristas (conexiones) entre los nodos
grafo.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "E"),
    ("D", "E")
])

# Definimos las restricciones para cada nodo
# Por ejemplo, el nodo "A" solo puede estar conectado con "B" y "C"
restricciones = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "E"],
    "D": ["B", "E"],
    "E": ["C", "D"]
}

# Aplicamos la propagación de restricciones al grafo
grafo_filtrado = propagacion_restricciones(grafo, restricciones)

# Dibujamos el grafo original
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
nx.draw(grafo, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
plt.title("Grafo Original")

# Dibujamos el grafo después de aplicar las restricciones
plt.subplot(1, 2, 2)
nx.draw(grafo_filtrado, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=2000, font_size=15)
plt.title("Grafo con Restricciones")

# Mostramos los grafos
plt.show()