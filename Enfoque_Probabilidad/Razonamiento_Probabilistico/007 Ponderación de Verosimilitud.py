import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# ---------------------------
# Definimos las probabilidades de la red bayesiana
# ---------------------------

# Probabilidad de lluvia
prob_lluvia = 0.3  # Probabilidad de que llueva
prob_no_lluvia = 1 - prob_lluvia  # Probabilidad de que no llueva

# Probabilidad de tráfico dado que llueve o no
prob_trafico_dado_lluvia = {
    True: 0.8,  # Si llueve, hay un 80% de probabilidad de tráfico
    False: 0.2  # Si no llueve, hay un 20% de probabilidad de tráfico
}

# Probabilidad de llegar tarde dado tráfico
prob_tarde_dado_trafico = {
    True: 0.9,  # Si hay tráfico, hay un 90% de probabilidad de llegar tarde
    False: 0.1  # Si no hay tráfico, solo un 10% de probabilidad de llegar tarde
}

# ---------------------------
# Función de Ponderación de Verosimilitud
# ---------------------------

def ponderacion_verosimilitud(n_muestras):
    """
    Esta función implementa el algoritmo de Ponderación de Verosimilitud
    para inferir la probabilidad de llegar tarde, dado que sabemos que llueve.
    """

    # Inicializamos las variables para contar las ponderaciones
    ponderacion_total = 0.0
    muestras_tarde = 0

    # Generamos las muestras
    for _ in range(n_muestras):
        # Muestrear 'Lluvia' (es una variable binaria: True o False)
        lluvia = np.random.rand() < prob_lluvia

        # Muestrear 'Trafico' dado 'Lluvia'
        trafico = np.random.rand() < prob_trafico_dado_lluvia[lluvia]

        # Muestrear 'Tarde' dado 'Trafico'
        tarde = np.random.rand() < prob_tarde_dado_trafico[trafico]

        # Verosimilitud: La probabilidad de que ocurra la muestra observada
        # Dado que sabemos que está lloviendo, solo tomamos el valor correspondiente de 'Lluvia'.
        verosimilitud = prob_lluvia if lluvia else prob_no_lluvia

        # Si la muestra es consistente con lo que sabemos (en este caso, si llueve)
        if lluvia:  # La condición de que sabemos que está lloviendo
            ponderacion_total += verosimilitud

            # Si la muestra también resulta en que llegamos tarde, incrementamos el contador
            if tarde:
                muestras_tarde += verosimilitud

    # Probabilidad marginal de llegar tarde, dada la información de que llueve
    probabilidad_tarde = muestras_tarde / ponderacion_total
    return probabilidad_tarde

# ---------------------------
# Ejecución del cálculo
# ---------------------------

# Número de muestras que queremos generar
n_muestras = 10000

# Calcular la probabilidad de llegar tarde usando Ponderación de Verosimilitud
prob_tarde = ponderacion_verosimilitud(n_muestras)
print(f"Probabilidad de llegar tarde dado que llueve: {prob_tarde:.4f}")

# ---------------------------
# Visualización de los resultados
# ---------------------------

def mostrar_grafo():
    """
    Función para mostrar un grafo simple de la red bayesiana.
    """
    # Usamos matplotlib para representar el grafo de la red bayesiana
    G = nx.DiGraph()

    # Nodos de la red
    G.add_node("Lluvia")
    G.add_node("Trafico")
    G.add_node("Tarde")

    # Relaciones de dependencia (arcos en el grafo)
    G.add_edge("Lluvia", "Trafico")
    G.add_edge("Trafico", "Tarde")

    # Posiciones de los nodos en el grafo
    pos = nx.spring_layout(G, seed=42)

    # Dibujamos el grafo
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold')
    nx.draw_networkx_edges(G, pos, arrowstyle='->', arrowsize=20)

    # Título de la gráfica
    plt.title("Red Bayesiana de Lluvia, Tráfico y Tarde")
    plt.show()

# Mostrar el grafo
mostrar_grafo()
