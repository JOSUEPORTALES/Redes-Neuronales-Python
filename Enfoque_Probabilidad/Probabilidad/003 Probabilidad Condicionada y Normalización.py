import networkx as nx
import matplotlib.pyplot as plt

# Probabilidades conocidas
# Probabilidad de que llueva
prob_lluvia = 0.3

# Probabilidad de que el cielo este nublado
prob_nublado = 0.5

# Probabilidad de que el sensor detecte lluvia cuando realmente llueve
prob_sensor_dado_lluvia = 0.9

# Probabilidad de que el sensor detecte lluvia cuando no esta lloviendo (falso positivo)
prob_sensor_dado_no_lluvia = 0.2

# Usamos el teorema de la probabilidad total para hallar:
# P(sensor=si) = P(sensor=si | lluvia) * P(lluvia) + P(sensor=si | no lluvia) * P(no lluvia)
prob_sensor = (prob_sensor_dado_lluvia * prob_lluvia) + (prob_sensor_dado_no_lluvia * (1 - prob_lluvia))

# Ahora aplicamos el teorema de Bayes:
# P(lluvia | sensor=si) = (P(sensor=si | lluvia) * P(lluvia)) / P(sensor=si)
prob_lluvia_dado_sensor = (prob_sensor_dado_lluvia * prob_lluvia) / prob_sensor

# Como tambien queremos la probabilidad de NO lluvia dado el sensor,
# usamos normalizacion en lugar de hacer otro calculo directo
prob_no_lluvia_dado_sensor = 1 - prob_lluvia_dado_sensor

# Guardamos los resultados en un diccionario para visualizarlos
probabilidades_condicionadas = {
    'Lluvia': prob_lluvia_dado_sensor,
    'No Lluvia': prob_no_lluvia_dado_sensor
}

# Imprimimos los resultados
print("Probabilidades condicionadas normalizadas dado que el sensor detecto lluvia:")
for evento, prob in probabilidades_condicionadas.items():
    print(f"{evento}: {prob:.3f}")

# ----------------------------
# GRAFO DE VISUALIZACION
# ----------------------------
def dibujar_grafo_probabilidades(probabilidades, sensor_activado=True):
    G = nx.DiGraph()

    # Nodo central representa la lectura del sensor
    evento_sensor = "Sensor: Detecta Lluvia" if sensor_activado else "Sensor: No Detecta"

    G.add_node(evento_sensor)
    for evento, prob in probabilidades.items():
        G.add_node(evento)
        G.add_edge(evento_sensor, evento, peso=round(prob, 2))

    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold')
    etiquetas = nx.get_edge_attributes(G, 'peso')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas)

    plt.title("Probabilidad Condicionada y Normalizacion")
    plt.show()

# Dibujamos el grafo
dibujar_grafo_probabilidades(probabilidades_condicionadas)
