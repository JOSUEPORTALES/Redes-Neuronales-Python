import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Definimos el entorno: una rejilla de 5x5 con algunos obstáculos
# 0: espacio libre, 1: obstáculo, 9: objetivo (recompensa)
entorno = np.array([
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 9, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0]
])

# Tamaño del entorno
filas, columnas = entorno.shape

# Definimos las acciones posibles (arriba, abajo, izquierda, derecha)
acciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # movimiento: arriba, abajo, izquierda, derecha

# Función para comprobar si una posición está dentro de los límites y no hay obstáculo
def es_valido(x, y):
    return 0 <= x < filas and 0 <= y < columnas and entorno[x, y] != 1

# Parámetros del algoritmo Q-learning
alpha = 0.1  # Tasa de aprendizaje
gamma = 0.9  # Factor de descuento
epsilon = 0.2  # Tasa de exploración (probabilidad de explorar en lugar de explotar)

# Inicializamos la tabla Q con valores arbitrarios (0 en este caso)
Q = np.zeros((filas, columnas, len(acciones)))

# Definimos la función de exploración/explotación
def seleccion_accion(x, y):
    if np.random.rand() < epsilon:
        # Exploración: elegimos una acción aleatoria
        accion = np.random.choice(len(acciones))
    else:
        # Explotación: elegimos la mejor acción según la tabla Q
        accion = np.argmax(Q[x, y])
    return accion

# Función de aprendizaje Q
def aprender():
    for episodio in range(1000):  # número de episodios
        # Comenzamos en una posición inicial (fuera de un obstáculo)
        x, y = 0, 0  # Posición inicial
        while True:
            # Seleccionamos una acción usando la política epsilon-greedy
            accion = seleccion_accion(x, y)
            dx, dy = acciones[accion]
            x_nueva, y_nueva = x + dx, y + dy
            
            # Verificamos si la nueva posición es válida
            if es_valido(x_nueva, y_nueva):
                x, y = x_nueva, y_nueva
            
            # Recompensa si llegamos al objetivo
            if entorno[x, y] == 9:
                recompensa = 10
                break  # Terminamos el episodio si llegamos al objetivo
            else:
                recompensa = -1  # Penalización por cada paso

            # Actualización de la tabla Q usando la fórmula de Q-learning
            siguiente_accion = np.argmax(Q[x, y])
            Q[x, y, accion] += alpha * (recompensa + gamma * Q[x, y, siguiente_accion] - Q[x, y, accion])

# Ejecutamos el aprendizaje
aprender()

# Función para mostrar la política aprendida (direcciones de la mejor acción)
def mostrar_politica():
    politica = np.full_like(entorno, '', dtype='<U10')
    for i in range(filas):
        for j in range(columnas):
            if entorno[i, j] != 1:  # No mostrar política para obstáculos
                mejor_accion = np.argmax(Q[i, j])
                if mejor_accion == 0:
                    politica[i, j] = 'Arriba'
                elif mejor_accion == 1:
                    politica[i, j] = 'Abajo'
                elif mejor_accion == 2:
                    politica[i, j] = 'Izquierda'
                elif mejor_accion == 3:
                    politica[i, j] = 'Derecha'
    print("Política aprendida:")
    for fila in politica:
        print(fila)

# Mostrar la política aprendida
mostrar_politica()

# Función para mostrar el grafo del entorno
def mostrar_grafo():
    G = nx.DiGraph()

    # Añadimos los nodos del grafo (cada celda en la rejilla)
    for i in range(filas):
        for j in range(columnas):
            if entorno[i, j] != 1:  # No añadimos nodos para los obstáculos
                G.add_node((i, j))

    # Añadimos las aristas para las conexiones válidas
    for i in range(filas):
        for j in range(columnas):
            if entorno[i, j] != 1:  # Si no es un obstáculo
                for accion in acciones:
                    x, y = i + accion[0], j + accion[1]
                    if es_valido(x, y):
                        G.add_edge((i, j), (x, y))

    # Dibujamos el grafo
    pos = {nodo: (nodo[1], -nodo[0]) for nodo in G.nodes()}  # Invertimos para mostrar bien la rejilla
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_size=10, font_weight='bold')
    plt.title("Grafo del Entorno - Aprendizaje por Refuerzo Activo")
    plt.show()

# Mostramos el grafo del entorno
mostrar_grafo()
