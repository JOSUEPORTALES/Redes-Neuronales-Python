# Importamos las librerías necesarias
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

# Creamos la red bayesiana
# En este ejemplo, modelamos el clima en dos momentos: clima_0 y clima_1
# Y definimos que clima_0 influye en clima_1
red = DiscreteBayesianNetwork([('clima_0', 'clima_1')])

# Definimos la CPD (tabla de probabilidad condicional) para clima_0
# Esto representa las probabilidades iniciales del clima
cpd_clima_0 = TabularCPD(
    variable='clima_0',
    variable_card=2,
    values=[[0.7], [0.3]],  # 70% soleado, 30% lluvioso
    state_names={'clima_0': ['soleado', 'lluvioso']}
)

# Definimos la CPD para clima_1 condicionado a clima_0
# Es decir, cómo cambia el clima de un día a otro
cpd_clima_1 = TabularCPD(
    variable='clima_1',
    variable_card=2,
    evidence=['clima_0'],
    evidence_card=[2],
    values=[
        [0.8, 0.3],  # P(soleado|soleado)=0.8, P(soleado|lluvioso)=0.3
        [0.2, 0.7]   # P(lluvioso|soleado)=0.2, P(lluvioso|lluvioso)=0.7
    ],
    state_names={
        'clima_1': ['soleado', 'lluvioso'],
        'clima_0': ['soleado', 'lluvioso']
    }
)

# Añadimos las CPDs a la red
red.add_cpds(cpd_clima_0, cpd_clima_1)

# Verificamos que la red sea válida
assert red.check_model()

# Creamos un objeto de inferencia para hacer consultas
inferencia = VariableElimination(red)

# Hacemos una consulta: ¿cuál es la probabilidad del clima_1 si clima_0 fue soleado?
resultado = inferencia.query(variables=['clima_1'], evidence={'clima_0': 'soleado'})

# Mostramos el resultado de la inferencia
print("Probabilidad del clima en t=1 dado que en t=0 fue soleado:")
print(resultado)

# Función para mostrar el grafo de la red
def mostrar_grafo(red):
    G = nx.DiGraph()
    G.add_edges_from(red.edges())

    # Dibujamos el grafo con NetworkX
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', arrows=True)
    plt.title("Red Bayesiana Dinámica (2 Tiempos)")
    plt.show()

# Llamamos a la función para graficar la red
mostrar_grafo(red)
