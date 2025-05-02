import matplotlib.pyplot as plt
import networkx as nx

# -------------------------------
# Probabilidades definidas
# -------------------------------

# Probabilidad de que llueva
prob_lluvia = 0.3
prob_no_lluvia = 1 - prob_lluvia

# Probabilidad de trafico dado lluvia
prob_trafico_dado_lluvia = {
    True: 0.8,   # Si llueve, mucho trafico
    False: 0.2   # Si no llueve, poco trafico
}

# Probabilidad de llegar tarde dado lluvia y trafico
prob_tarde_dado_lluvia_trafico = {
    (True, True): 0.9,
    (True, False): 0.5,
    (False, True): 0.6,
    (False, False): 0.1
}

# -------------------------------
# Calculo con la Regla de la Cadena
# -------------------------------

# Recorremos todas las combinaciones posibles
print("\nProbabilidades conjuntas usando la regla de la cadena:\n")

for lluvia in [True, False]:
    for trafico in [True, False]:
        for tarde in [True, False]:
            # Paso 1: P(lluvia)
            p1 = prob_lluvia if lluvia else prob_no_lluvia
            
            # Paso 2: P(trafico | lluvia)
            p2 = prob_trafico_dado_lluvia[lluvia] if trafico else (1 - prob_trafico_dado_lluvia[lluvia])
            
            # Paso 3: P(tarde | lluvia, trafico)
            p3 = prob_tarde_dado_lluvia_trafico[(lluvia, trafico)] if tarde else (1 - prob_tarde_dado_lluvia_trafico[(lluvia, trafico)])
            
            # Probabilidad conjunta
            prob_conjunta = p1 * p2 * p3
            
            print(f"Lluvia: {lluvia}, Trafico: {trafico}, Tarde: {tarde} → Prob: {prob_conjunta:.4f}")

# -------------------------------
# Visualizacion del grafo
# -------------------------------

def mostrar_red_cadena():
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

    plt.title("Grafo - Regla de la Cadena (Lluvia, Trafico, Tarde)")
    plt.show()

# Mostrar grafo
mostrar_red_cadena()
