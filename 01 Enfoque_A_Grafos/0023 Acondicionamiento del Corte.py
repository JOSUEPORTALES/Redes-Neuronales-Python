import networkx as nx
"""
Este programa utiliza la biblioteca NetworkX para crear y analizar un grafo no dirigido. 
El objetivo principal es identificar nodos en conflicto, es decir, nodos conectados por 
una arista que tienen el mismo valor en su atributo 'valor'. Los pasos principales son:
1. Crear un grafo y agregar nodos con atributos personalizados.
2. Definir las conexiones (aristas) entre los nodos.
3. Analizar las aristas para encontrar nodos que violan la restricción de valores iguales.
4. Generar una lista de nodos en conflicto, eliminando duplicados.
5. Mostrar los nodos que necesitan ser "acondicionados" (modificados o desconectados).
Este análisis puede ser útil en problemas de optimización o en la detección de conflictos 
en redes donde ciertos atributos no deben coincidir entre nodos conectados.
"""




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
