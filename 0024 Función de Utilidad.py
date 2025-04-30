import networkx as nx

# Crear un grafo dirigido (las decisiones tienen dirección)
G = nx.DiGraph()

# Agregar nodos con utilidad (atributo)
G.add_node("A", utilidad=10)   # Estado A: utilidad 10
G.add_node("B", utilidad=15)   # Estado B: utilidad 15
G.add_node("C", utilidad=8)    # Estado C: utilidad 8
G.add_node("D", utilidad=20)   # Estado D: utilidad 20

# Agregar decisiones posibles (caminos del agente)
G.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D")
])

# Mostrar las utilidades de cada nodo
print("Utilidades de cada estado:")
for nodo in G.nodes():
    print(f"{nodo}: utilidad = {G.nodes[nodo]['utilidad']}")

# Encontrar el nodo con mayor utilidad
mejor_estado = max(G.nodes, key=lambda n: G.nodes[n]['utilidad'])
print("\n🟢 Mejor estado según utilidad:", mejor_estado)
print("🔢 Utilidad máxima:", G.nodes[mejor_estado]['utilidad'])
