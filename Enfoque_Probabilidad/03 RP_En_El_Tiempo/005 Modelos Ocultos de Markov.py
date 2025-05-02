import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# ----------------------------------------------
# Definimos los estados ocultos del sistema
# ----------------------------------------------
estados = ['lluvioso', 'soleado']

# Observaciones que podemos ver
observaciones_posibles = ['paraguas', 'sin_paraguas']

# Probabilidad inicial de cada estado (el primer dia)
probabilidad_inicial = {
    'lluvioso': 0.6,
    'soleado': 0.4
}

# Probabilidades de transicion entre estados de un dia a otro
transicion = {
    'lluvioso': {'lluvioso': 0.7, 'soleado': 0.3},
    'soleado': {'lluvioso': 0.4, 'soleado': 0.6}
}

# Probabilidades de observacion (paraguas o no) segun el estado del clima
emision = {
    'lluvioso': {'paraguas': 0.9, 'sin_paraguas': 0.1},
    'soleado': {'paraguas': 0.2, 'sin_paraguas': 0.8}
}

# Secuencia de observaciones durante 5 dias
secuencia_observada = ['paraguas', 'paraguas', 'sin_paraguas', 'paraguas', 'paraguas']

# ----------------------------------------------
# Algoritmo hacia adelante (forward)
# ----------------------------------------------
def algoritmo_adelante(observaciones, estados, prob_ini, trans, emis):
    paso_adelante = []

    # Dia 1: multiplicamos la probabilidad inicial por la probabilidad de observacion
    estado_actual = {
        estado: prob_ini[estado] * emis[estado][observaciones[0]]
        for estado in estados
    }

    # Normalizamos las probabilidades
    suma = sum(estado_actual.values())
    for estado in estado_actual:
        estado_actual[estado] /= suma

    paso_adelante.append(estado_actual.copy())

    # Para los siguientes dias
    for observacion in observaciones[1:]:
        nuevo_estado = {}
        for estado in estados:
            # Suma de probabilidades ponderadas desde los estados anteriores
            suma = sum(
                paso_adelante[-1][estado_anterior] * trans[estado_anterior][estado]
                for estado_anterior in estados
            )
            nuevo_estado[estado] = emis[estado][observacion] * suma

        # Normalizamos
        suma_total = sum(nuevo_estado.values())
        for estado in nuevo_estado:
            nuevo_estado[estado] /= suma_total

        paso_adelante.append(nuevo_estado.copy())

    return paso_adelante

# ----------------------------------------------
# Funcion para graficar la red de inferencia
# ----------------------------------------------
def graficar_red(estimacion_estados, observaciones):
    G = nx.DiGraph()

    dias = len(observaciones)
    for dia in range(dias):
        for estado in estados:
            nombre_nodo = f"{estado}_{dia}"
            G.add_node(nombre_nodo, label=estado, layer=dia)

            if dia > 0:
                for estado_anterior in estados:
                    nodo_anterior = f"{estado_anterior}_{dia - 1}"
                    G.add_edge(nodo_anterior, nombre_nodo)

    # Posiciones de los nodos para graficar por capas
    posicion = {}
    for i, (dia, obs) in enumerate(zip(range(dias), observaciones)):
        for j, estado in enumerate(estados):
            posicion[f"{estado}_{dia}"] = (dia, j)

    # Dibujamos el grafo
    plt.figure(figsize=(12, 5))
    nx.draw(G, posicion, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')

    # Mostrar probabilidades como etiquetas
    etiquetas = {
        f"{estado}_{i}": f"{estado}\n{estimacion_estados[i][estado]:.2f}"
        for i in range(dias)
        for estado in estados
    }

    nx.draw_networkx_labels(G, posicion, labels=etiquetas, font_color='black')
    plt.title("Red de Inferencia - Modelo Oculto de Markov")
    plt.axis('off')
    plt.show()

# ----------------------------------------------
# Programa principal
# ----------------------------------------------
if __name__ == "__main__":
    print("Modelo Oculto de Markov: Inferencia usando el algoritmo hacia adelante\n")

    resultado = algoritmo_adelante(secuencia_observada, estados, probabilidad_inicial, transicion, emision)

    # Mostramos los resultados en consola
    for i, dia in enumerate(resultado):
        print(f"Dia {i+1}:")
        for estado in estados:
            print(f"  {estado}: {dia[estado]:.4f}")

    # Graficamos la red
    graficar_red(resultado, secuencia_observada)
