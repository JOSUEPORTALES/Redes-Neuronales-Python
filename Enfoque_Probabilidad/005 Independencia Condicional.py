import matplotlib.pyplot as plt
import networkx as nx

# Probabilidades bases (supuestas)
prob_robo = 0.01
prob_terremoto = 0.02

# Probabilidad de que la alarma suene si hay un robo y/o terremoto
# Se simplifica a combinaciones posibles
prob_alarma_dado_robo_terremoto = {
    (True, True): 0.95,
    (True, False): 0.94,
    (False, True): 0.29,
    (False, False): 0.001
}

# Probabilidad de que un vecino llame si escucha la alarma
prob_vecino1_dado_alarma = {True: 0.9, False: 0.05}
prob_vecino2_dado_alarma = {True: 0.8, False: 0.1}

# Para este ejemplo, asumimos que sabemos que la alarma sonó.
alarma_sono = True

# Calculamos las probabilidades individuales de que cada vecino llame dado que sono la alarma
prob_llamada_vecino1 = prob_vecino1_dado_alarma[alarma_sono]
prob_llamada_vecino2 = prob_vecino2_dado_alarma[alarma_sono]

# Como queremos saber si las llamadas son condicionalmente independientes:
# Calculamos la probabilidad conjunta:
# P(vecino1 y vecino2 | alarma) = P(vecino1 | alarma) * P(vecino2 | alarma)
prob_conjunta = prob_llamada_vecino1 * prob_llamada_vecino2

# Imprimimos los resultados
print("Probabilidad de que el vecino 1 llame dado que sono la alarma:", prob_llamada_vecino1)
print("Probabilidad de que el vecino 2 llame dado que sono la alarma:", prob_llamada_vecino2)
print("Probabilidad conjunta de ambas llamadas dado que sono la alarma:", prob_conjunta)

# -------------------------------------------------
# VISUALIZACION CON GRAFO
# -------------------------------------------------
def grafo_independencia_condicional():
    G = nx.DiGraph()

    # Nodos del modelo
    G.add_node("Robo")
    G.add_node("Terremoto")
    G.add_node("Alarma")
    G.add_node("Vecino 1 llama")
    G.add_node("Vecino 2 llama")

    # Relaciones de dependencia
    G.add_edge("Robo", "Alarma")
    G.add_edge("Terremoto", "Alarma")
    G.add_edge("Alarma", "Vecino 1 llama")
    G.add_edge("Alarma", "Vecino 2 llama")

    # Dibujamos el grafo
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightgreen', font_weight='bold', arrows=True)

    plt.title("Independencia Condicional: Vecinos | Alarma")
    plt.show()

# Mostrar el grafo
grafo_independencia_condicional()
