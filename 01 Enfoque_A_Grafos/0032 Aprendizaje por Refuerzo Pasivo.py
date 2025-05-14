import numpy as np
"""
Este programa implementa un enfoque de aprendizaje por refuerzo pasivo en un entorno de rejilla 5x5.
El objetivo es calcular los valores de los estados (V(s)) utilizando una política fija y evaluar
la función de valor hasta la convergencia. El entorno incluye obstáculos y un objetivo con recompensa.
Funciones principales:
- `es_valido(x, y)`: Comprueba si una posición está dentro de los límites del entorno y no es un obstáculo.
- `evaluacion_politica()`: Realiza la evaluación de política iterativa para calcular los valores de los estados.
- `mostrar_rejilla()`: Muestra en consola los valores calculados para cada estado en la rejilla.
- `mostrar_grafo()`: Genera y visualiza un grafo que representa el entorno, donde los nodos son las celdas
    y las aristas representan las conexiones válidas entre ellas.
Parámetros importantes:
- `entorno`: Matriz que define el entorno (0: espacio libre, 1: obstáculo, 9: objetivo).
- `gamma`: Factor de descuento para las recompensas futuras.
- `recompensa_objetivo`: Recompensa asignada al estado objetivo.
El programa utiliza librerías como `numpy` para cálculos matriciales, `matplotlib` para visualización,
y `networkx` para la representación del grafo del entorno.
"""
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

# Inicializamos la matriz de valores V(s) para cada estado
V = np.zeros_like(entorno, dtype=float)

# Definimos el factor de descuento (gamma) y la recompensa
gamma = 0.9  # Descuento de las recompensas futuras
recompensa_objetivo = 10  # Recompensa cuando llegamos al objetivo

# Función para hacer la evaluación de política
def evaluacion_politica():
    # Inicializamos el valor de la función en todos los estados
    iteraciones = 0
    while True:
        iteraciones += 1
        V_nueva = np.copy(V)  # Copia de los valores actuales
        cambio = 0  # Verificamos cuánto cambiaron los valores

        for i in range(filas):
            for j in range(columnas):
                if entorno[i, j] == 1:  # Si hay un obstáculo, no hacemos nada
                    continue
                # Si es el objetivo, asignamos la recompensa
                if entorno[i, j] == 9:
                    V_nueva[i, j] = recompensa_objetivo
                    continue
                
                # Calculamos el valor para cada acción
                valores_acciones = []
                for accion in acciones:
                    x, y = i + accion[0], j + accion[1]
                    if es_valido(x, y):
                        valores_acciones.append(V[x, y])
                    else:
                        valores_acciones.append(V[i, j])  # Si la acción es inválida, mantenemos el valor actual
                
                # El valor de un estado es el valor máximo de sus posibles acciones
                V_nueva[i, j] = np.max(valores_acciones)
                cambio += abs(V[i, j] - V_nueva[i, j])

        # Actualizamos los valores de la función V
        V[:] = V_nueva
        if cambio < 0.01:  # Convergencia, cuando el cambio es pequeño
            break

        if iteraciones > 100:
            break

# Ejecutamos la evaluación de política
evaluacion_politica()

# Función para mostrar el valor de la rejilla en la consola
def mostrar_rejilla():
    for fila in V:
        print(" ".join([f"{v:.2f}" for v in fila]))

# Mostrar los valores de cada estado
print("Valores de los estados:")
mostrar_rejilla()

# Graficamos el grafo del entorno
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
    plt.title("Grafo del Entorno - Red Bayesiana Dinámica")
    plt.show()

# Mostramos el grafo del entorno
mostrar_grafo()
