import matplotlib.pyplot as plt
import networkx as nx

# -------------------------------
# Definimos las probabilidades base
# -------------------------------

# Probabilidad de que una persona tenga la enfermedad (P(A))
prob_enfermedad = 0.01

# Probabilidad de que una persona NO tenga la enfermedad
prob_no_enfermedad = 1 - prob_enfermedad

# Probabilidad de que el test de positivo si la persona TIENE la enfermedad (P(B|A))
prob_test_positivo_si_enfermo = 0.99

# Probabilidad de que el test de positivo si la persona NO TIENE la enfermedad (P(B|¬A))
prob_test_positivo_si_sano = 0.05

# -------------------------------
# Aplicamos la Regla de Bayes
# -------------------------------

# Calculamos la probabilidad total de test positivo: P(B)
prob_test_positivo = (
    prob_test_positivo_si_enfermo * prob_enfermedad +
    prob_test_positivo_si_sano * prob_no_enfermedad
)

# Usamos la regla de Bayes para calcular: P(A|B)
prob_enfermedad_dado_positivo = (
    prob_test_positivo_si_enfermo * prob_enfermedad
) / prob_test_positivo

# -------------------------------
# Mostramos el resultado
# -------------------------------
print("Probabilidad de tener la enfermedad dado un test positivo:")
print(f"P(Enfermedad | Test Positivo) = {prob_enfermedad_dado_positivo:.4f}")

# -------------------------------
# Grafo para visualizar la relación
# -------------------------------
def grafo_regla_bayes():
    G = nx.DiGraph()

    # Nodos
    G.add_node("Enfermedad")
    G.add_node("No Enfermedad")
    G.add_node("Test Positivo")

    # Aristas con pesos (no se usan para calcular, solo para mostrar)
    G.add_edge("Enfermedad", "Test Positivo", peso=prob_test_positivo_si_enfermo)
    G.add_edge("No Enfermedad", "Test Positivo", peso=prob_test_positivo_si_sano)

    pos = nx.spring_layout(G, seed=42)
    etiquetas = nx.get_edge_attributes(G, 'peso')
    etiquetas_formato = {arista: f"P={peso:.2f}" for arista, peso in etiquetas.items()}

    # Dibujamos el grafo
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=etiquetas_formato)

    plt.title("Grafo de la Regla de Bayes")
    plt.show()

# Llamamos la funcion para mostrar el grafo
grafo_regla_bayes()
