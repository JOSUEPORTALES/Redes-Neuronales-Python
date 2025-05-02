import networkx as nx
import matplotlib.pyplot as plt

# ---------------------------
# Definimos las probabilidades
# ---------------------------

# Probabilidad de lluvia
prob_lluvia = 0.3
prob_no_lluvia = 1 - prob_lluvia

# Probabilidad de tráfico dado lluvia
prob_trafico_dado_lluvia = {
    True: 0.8,   # Si llueve, mucho tráfico
    False: 0.2   # Si no llueve, poco tráfico
}

# Probabilidad de llegar tarde dado tráfico y lluvia
prob_tarde_dado_lluvia_trafico = {
    (True, True): 0.9,  # Si llueve y hay tráfico, es muy probable que llegues tarde
    (True, False): 0.5, # Si llueve y no hay tráfico, la probabilidad de llegar tarde es media
    (False, True): 0.6, # Si no llueve pero hay tráfico, es más probable que llegues tarde
    (False, False): 0.1 # Si no hay lluvia y no hay tráfico, es poco probable que llegues tarde
}

# ---------------------------
# Función de eliminación de variables
# ---------------------------

def eliminacion_variables():
    """
    Función para calcular la probabilidad de 'Tarde' marginalizando sobre
    las variables 'Lluvia' y 'Trafico'.
    """
    probabilidad_tarde = 0.0

    # Primero, eliminamos 'Lluvia' (sumamos sobre todos sus valores)
    for lluvia in [True, False]:  # Recorrer todas las posibilidades de 'Lluvia'
        for trafico in [True, False]:  # Recorrer todas las posibilidades de 'Trafico'
            # Calculamos la probabilidad conjunta de 'Trafico' y 'Tarde'
            prob_lluvia_actual = prob_lluvia if lluvia else prob_no_lluvia
            prob_trafico = prob_trafico_dado_lluvia[lluvia] if trafico else (1 - prob_trafico_dado_lluvia[lluvia])

            # Calculamos la probabilidad de 'Tarde' dado 'Trafico' y 'Lluvia'
            prob_tarde = prob_tarde_dado_lluvia_trafico[(lluvia, trafico)]

            # Calculamos la probabilidad conjunta de todos estos eventos
            probabilidad_conjunta = prob_lluvia_actual * prob_trafico * prob_tarde

            # Sumamos esta probabilidad al total
            probabilidad_tarde += probabilidad_conjunta

    return probabilidad_tarde

# ---------------------------
# Ejecución del cálculo
# ---------------------------

# Queremos saber la probabilidad de llegar tarde después de eliminar las variables 'Lluvia' y 'Trafico'
prob_tarde_marginalizada = eliminacion_variables()
print(f"Probabilidad de llegar tarde después de eliminar las variables 'Lluvia' y 'Trafico': {prob_tarde_marginalizada:.4f}")

# ---------------------------
# Visualizamos el grafo de la red bayesiana
# ---------------------------

def mostrar_grafo():
    G = nx.DiGraph()

    # Nodos
    G.add_node("Lluvia")
    G.add_node("Trafico")
    G.add_node("Tarde")

    # Relaciones de dependencia
    G.add_edge("Lluvia", "Trafico")
    G.add_edge("Lluvia", "Tarde")
    G.add_edge("Trafico", "Tarde")

    # Posiciones de los nodos
    pos = nx.spring_layout(G, seed=5)

    # Dibujamos el grafo
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold')
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)

    plt.title("Red Bayesiana - Eliminación de Variables")
    plt.show()

# Mostrar el grafo
mostrar_grafo()
