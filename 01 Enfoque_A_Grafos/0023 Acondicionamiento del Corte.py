import networkx as nx

# Crear el grafo
G = nx.Graph()

# Agregar nodos con atributos
G.add_node(1, valor=5)
G.add_node(2, valor=3)
G.add_node(3, valor=5)
G.add_node(4, valor=2)

# Agregar aristas (conexiones entre nodos)
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Encontrar nodos que violan la restricción
nodos_en_conflicto = []
for u, v in G.edges():
    if G.nodes[u]['valor'] == G.nodes[v]['valor']:
        nodos_en_conflicto.extend([u, v])

# Eliminar duplicados
nodos_en_conflicto = list(set(nodos_en_conflicto))

# Mostrar nodos que hay que "acondicionar"
print("Nodos en conflicto (para cortar o modificar):", nodos_en_conflicto)
