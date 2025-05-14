import networkx as nx
"""
Este programa utiliza la biblioteca NetworkX para modelar un grafo dirigido que representa
un conjunto de estados y decisiones posibles entre ellos. Cada nodo del grafo tiene un
atributo de utilidad asociado, que indica el valor o beneficio de estar en ese estado.
El programa realiza las siguientes operaciones:
1. Crea un grafo dirigido (DiGraph) para modelar las decisiones con dirección.
2. Agrega nodos al grafo, asignando a cada uno una utilidad específica.
3. Define las conexiones (aristas) entre los nodos, representando las decisiones posibles.
4. Muestra las utilidades de cada nodo en la consola.
5. Encuentra y muestra el nodo con la mayor utilidad, junto con su valor.
Este enfoque puede ser útil en problemas de toma de decisiones, donde se busca maximizar
la utilidad al elegir entre diferentes opciones.
"""





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
