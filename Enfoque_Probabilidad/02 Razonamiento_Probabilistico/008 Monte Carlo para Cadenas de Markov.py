import numpy as np
import matplotlib.pyplot as plt
import networkx as nx  # Para visualizar el grafo

# ---------------------------
# Definición de la cadena de Markov
# ---------------------------

# Definimos las probabilidades de transición entre estados
# P(A->A), P(A->B), P(B->A), P(B->B)
probabilidades_transicion = {
    "A": {"A": 0.7, "B": 0.3},  # Si estamos en A, 70% de permanecer en A y 30% de pasar a B
    "B": {"A": 0.4, "B": 0.6}   # Si estamos en B, 40% de pasar a A y 60% de permanecer en B
}

# Número de pasos para la simulación
num_pasos = 100

# Número de simulaciones para usar en Monte Carlo
num_simulaciones = 10000

# ---------------------------
# Función para simular la cadena de Markov
# ---------------------------

def simular_cadena_markov(inicio, num_pasos, probabilidades_transicion):
    """
    Esta función simula la evolución de la cadena de Markov
    durante un número dado de pasos y retorna el estado final
    al que llegó el sistema.
    """
    estado_actual = inicio
    for _ in range(num_pasos):
        # Se elige el siguiente estado según las probabilidades de transición
        siguiente_estado = np.random.choice(
            ["A", "B"],  # Posibles estados
            p=[probabilidades_transicion[estado_actual]["A"], probabilidades_transicion[estado_actual]["B"]]
        )
        estado_actual = siguiente_estado  # Actualizamos el estado
    return estado_actual

# ---------------------------
# Método de Monte Carlo para estimar la probabilidad de los estados
# ---------------------------

def monte_carlo(num_simulaciones, num_pasos, probabilidades_transicion):
    """
    Función que utiliza el método de Monte Carlo para estimar
    la probabilidad de estar en cada uno de los estados después
    de un número dado de pasos en una cadena de Markov.
    """
    # Contadores para el número de veces que terminamos en A o B
    contador_A = 0
    contador_B = 0

    for _ in range(num_simulaciones):
        # Simulamos una cadena de Markov comenzando en A
        estado_final = simular_cadena_markov("A", num_pasos, probabilidades_transicion)

        # Contamos en qué estado termina la simulación
        if estado_final == "A":
            contador_A += 1
        else:
            contador_B += 1

    # Estimamos las probabilidades basadas en las simulaciones
    probabilidad_A = contador_A / num_simulaciones
    probabilidad_B = contador_B / num_simulaciones

    return probabilidad_A, probabilidad_B

# ---------------------------
# Ejecución del método de Monte Carlo
# ---------------------------

prob_A, prob_B = monte_carlo(num_simulaciones, num_pasos, probabilidades_transicion)

# Imprimimos los resultados
print(f"Probabilidad de estar en el estado A después de {num_pasos} pasos: {prob_A:.4f}")
print(f"Probabilidad de estar en el estado B después de {num_pasos} pasos: {prob_B:.4f}")

# ---------------------------
# Visualización del grafo de la cadena de Markov
# ---------------------------

def mostrar_grafo():
    """
    Función para mostrar un grafo simple de la cadena de Markov.
    """
    G = nx.DiGraph()  # Grafo dirigido para mostrar las transiciones

    # Nodos de la cadena (estados A y B)
    G.add_node("A")
    G.add_node("B")

    # Arcos de las transiciones, con sus probabilidades
    G.add_edge("A", "A", weight=0.7)
    G.add_edge("A", "B", weight=0.3)
    G.add_edge("B", "A", weight=0.4)
    G.add_edge("B", "B", weight=0.6)

    # Posiciones de los nodos
    pos = nx.spring_layout(G, seed=42)

    # Dibujamos el grafo
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_weight='bold')
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Título
    plt.title("Cadena de Markov: Transiciones entre A y B")
    plt.show()

# Mostrar el grafo de la cadena de Markov
mostrar_grafo()
