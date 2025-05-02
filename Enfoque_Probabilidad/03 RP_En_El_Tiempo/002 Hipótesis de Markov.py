import random
import networkx as nx
import matplotlib.pyplot as plt

# --------------------------------------------
# Definimos el espacio de estados y transiciones
# --------------------------------------------

# Diccionario donde cada estado tiene probabilidades de transicion
matriz_transicion = {
    'Soleado': {'Soleado': 0.8, 'Lluvioso': 0.2},
    'Lluvioso': {'Soleado': 0.4, 'Lluvioso': 0.6}
}

# --------------------------------------------
# Funcion para elegir el siguiente estado
# segun las probabilidades definidas
# --------------------------------------------

def transicion(estado_actual):
    """
    Escoge el siguiente estado basado en las probabilidades
    del estado actual usando la hipotesis de Markov.
    """
    estados_posibles = list(matriz_transicion[estado_actual].keys())
    probabilidades = list(matriz_transicion[estado_actual].values())
    siguiente_estado = random.choices(estados_posibles, weights=probabilidades, k=1)[0]
    return siguiente_estado

# --------------------------------------------
# Simulacion del proceso de Markov
# --------------------------------------------

def simular_proceso(inicio, pasos):
    """
    Simula una cadena de Markov desde un estado inicial
    durante un numero dado de pasos.
    """
    trayectoria = [inicio]
    estado_actual = inicio

    for _ in range(pasos):
        estado_actual = transicion(estado_actual)
        trayectoria.append(estado_actual)

    return trayectoria

# --------------------------------------------
# Dibujamos el grafo del proceso de Markov
# --------------------------------------------

def graficar_proceso():
    """
    Crea y muestra un grafo dirigido con las probabilidades
    de transicion entre estados.
    """
    grafo = nx.DiGraph()

    # Agregamos nodos y aristas al grafo con etiquetas
    for origen, destinos in matriz_transicion.items():
        for destino, probabilidad in destinos.items():
            grafo.add_edge(origen, destino, label=str(probabilidad))

    # Posiciones de los nodos
    posiciones = nx.spring_layout(grafo)
    
    # Dibujamos nodos y aristas
    nx.draw(grafo, posiciones, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, arrows=True)
    
    # Dibujamos las etiquetas de probabilidad en las aristas
    etiquetas = nx.get_edge_attributes(grafo, 'label')
    nx.draw_networkx_edge_labels(grafo, posiciones, edge_labels=etiquetas)

    plt.title("Proceso de Markov: Clima")
    plt.show()

# --------------------------------------------
# Ejecutamos la simulacion y la graficacion
# --------------------------------------------

estado_inicial = 'Soleado'
numero_pasos = 10

trayectoria = simular_proceso(estado_inicial, numero_pasos)

print("Trayectoria simulada del clima:")
print(" -> ".join(trayectoria))

graficar_proceso()
