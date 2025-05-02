"""Situación:
Si hay un robo o un terremoto, suena una alarma.

Dos vecinos (Juan y Ana) pueden llamar si oyen la alarma.

Queremos calcular:
¿Cuál es la probabilidad de que haya un robo si Juan llama y Ana llama?
"""

import matplotlib.pyplot as plt
import networkx as nx

# -------------------------------
# 1. Probabilidades base (tablas de probabilidad condicional)
# -------------------------------

# P(robo)
prob_robo = 0.01
prob_no_robo = 1 - prob_robo

# P(terremoto)
prob_terremoto = 0.02
prob_no_terremoto = 1 - prob_terremoto

# P(alarma | robo, terremoto)
prob_alarma = {
    (True, True): 0.95,
    (True, False): 0.94,
    (False, True): 0.29,
    (False, False): 0.001
}

# P(llamada_juan | alarma)
prob_llamada_juan = {True: 0.90, False: 0.05}

# P(llamada_ana | alarma)
prob_llamada_ana = {True: 0.70, False: 0.01}

# -------------------------------
# 2. Inferencia manual simple con casos posibles
# -------------------------------

# Creamos todas las combinaciones posibles de los eventos
combinaciones = []

# Iteramos sobre todas las combinaciones posibles de verdad/falso para las variables
for robo in [True, False]:
    for terremoto in [True, False]:
        alarma = prob_alarma[(robo, terremoto)]
        for a in [True, False]:
            for b in [True, False]:
                # Calculamos la probabilidad conjunta
                probabilidad = (
                    (prob_robo if robo else prob_no_robo) *
                    (prob_terremoto if terremoto else prob_no_terremoto) *
                    alarma if a else (1 - alarma) *
                    prob_llamada_juan[a] *
                    prob_llamada_ana[b]
                )
                combinaciones.append({
                    'robo': robo,
                    'terremoto': terremoto,
                    'alarma': a,
                    'juan_llama': a,
                    'ana_llama': b,
                    'probabilidad': probabilidad
                })

# Filtramos las combinaciones donde Juan y Ana llaman
evidencia = [c for c in combinaciones if c['juan_llama'] and c['ana_llama']]

# Normalizamos la probabilidad
suma_probabilidades = sum(c['probabilidad'] for c in evidencia)

# Calculamos P(robo | juan_llama, ana_llama)
prob_robo_dado_llamadas = sum(
    c['probabilidad'] for c in evidencia if c['robo']
) / suma_probabilidades

print(f"\nProbabilidad de ROBO dado que Juan y Ana llaman: {prob_robo_dado_llamadas:.4f}")

# -------------------------------
# 3. Visualizamos la Red Bayesiana
# -------------------------------

def grafo_red_bayesiana():
    G = nx.DiGraph()

    # Nodos
    G.add_node("Robo")
    G.add_node("Terremoto")
    G.add_node("Alarma")
    G.add_node("Juan llama")
    G.add_node("Ana llama")

    # Aristas: relaciones de dependencia
    G.add_edge("Robo", "Alarma")
    G.add_edge("Terremoto", "Alarma")
    G.add_edge("Alarma", "Juan llama")
    G.add_edge("Alarma", "Ana llama")

    # Dibujamos el grafo
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightyellow', node_size=2000, font_weight='bold')
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)

    plt.title("Red Bayesiana - Ejemplo de Alarma")
    plt.show()

# Mostrar el grafo
grafo_red_bayesiana()




