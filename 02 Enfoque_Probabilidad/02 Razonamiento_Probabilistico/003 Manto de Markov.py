import networkx as nx
import matplotlib.pyplot as plt

# Creamos el grafo dirigido para representar la red bayesiana
grafo = nx.DiGraph()

# Agregamos nodos que representan variables
nodos = ["Gen", "Fumar", "Cancer", "Radiografia", "Fatiga"]
grafo.add_nodes_from(nodos)

# Agregamos las relaciones de dependencia (aristas dirigidas)
grafo.add_edges_from([
    ("Gen", "Cancer"),
    ("Fumar", "Cancer"),
    ("Cancer", "Radiografia"),
    ("Cancer", "Fatiga")
])

# Funcion para obtener el manto de Markov de un nodo
def obtener_manto_markov(grafo, nodo_objetivo):
    padres = set(grafo.predecessors(nodo_objetivo))  # Padres directos
    hijos = set(grafo.successors(nodo_objetivo))     # Hijos directos
    
    # Padres de los hijos (excepto el nodo objetivo)
    padres_de_hijos = set()
    for hijo in hijos:
        padres_hijo = set(grafo.predecessors(hijo))
        padres_de_hijos.update(padres_hijo)
    
    # Remover el nodo objetivo para no incluirlo dos veces
    padres_de_hijos.discard(nodo_objetivo)
    
    # Union de padres, hijos y padres de hijos
    manto = padres.union(hijos).union(padres_de_hijos)
    return manto

# Elegimos el nodo para el cual queremos el manto de Markov
nodo = "Cancer"
manto = obtener_manto_markov(grafo, nodo)

# Mostramos el resultado
print(f"\nManto de Markov del nodo '{nodo}': {manto}\n")

# ----------------------------------------
# Visualizamos el grafo y destacamos el manto
# ----------------------------------------

def mostrar_grafo_con_manto(grafo, nodo_objetivo, manto):
    colores = []
    for nodo in grafo.nodes:
        if nodo == nodo_objetivo:
            colores.append("red")  # Nodo central
        elif nodo in manto:
            colores.append("orange")  # Manto de Markov
        else:
            colores.append("lightblue")  # Otros nodos

    pos = nx.spring_layout(grafo, seed=7)
    nx.draw(grafo, pos, with_labels=True, node_color=colores, node_size=2000, font_weight='bold', arrows=True)
    plt.title(f"Grafo con Manto de Markov de '{nodo_objetivo}'")
    plt.show()

# Llamamos a la funcion para mostrar el grafo
mostrar_grafo_con_manto(grafo, nodo, manto)
