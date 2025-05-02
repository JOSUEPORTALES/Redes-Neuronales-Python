import random
import networkx as nx

# Importamos las librerías necesarias
import matplotlib.pyplot as plt

# Función para calcular los conflictos en un estado
def calcular_conflictos(estado, restricciones):
    """
    Calcula el número de conflictos en un estado dado.
    Un conflicto ocurre cuando una restricción no se cumple.

    estado: diccionario que representa el estado actual.
    restricciones: lista de pares que representan las restricciones entre nodos.
    """
    conflictos = 0
    for (nodo1, nodo2) in restricciones:
        if estado[nodo1] == estado[nodo2]:  # Si dos nodos tienen el mismo valor, hay un conflicto
            conflictos += 1
    return conflictos

# Algoritmo de mínimos conflictos
def minimos_conflictos(nodos, restricciones, max_iteraciones=1000):
    """
    Implementa el algoritmo de mínimos conflictos para resolver un problema de satisfacción de restricciones.

    nodos: lista de nodos del grafo.
    restricciones: lista de pares que representan las restricciones entre nodos.
    max_iteraciones: número máximo de iteraciones para intentar encontrar una solución.
    """
    # Inicializamos el estado asignando valores aleatorios a cada nodo
    estado = {nodo: random.choice([0, 1]) for nodo in nodos}

    for _ in range(max_iteraciones):
        # Calculamos el número de conflictos en el estado actual
        conflictos_totales = calcular_conflictos(estado, restricciones)
        if conflictos_totales == 0:  # Si no hay conflictos, hemos encontrado una solución
            return estado

        # Elegimos un nodo en conflicto al azar
        nodo_en_conflicto = random.choice([
            nodo for nodo in nodos
            if any(estado[nodo] == estado[vecino] for vecino in nodos if (nodo, vecino) in restricciones or (vecino, nodo) in restricciones)
        ])

        # Probamos asignar un nuevo valor al nodo para minimizar los conflictos
        mejor_valor = estado[nodo_en_conflicto]
        menor_conflicto = float('inf')
        for valor in [0, 1]:
            estado[nodo_en_conflicto] = valor
            conflictos = calcular_conflictos(estado, restricciones)
            if conflictos < menor_conflicto:
                menor_conflicto = conflictos
                mejor_valor = valor

        # Asignamos el mejor valor encontrado
        estado[nodo_en_conflicto] = mejor_valor

    # Si llegamos aquí, no encontramos solución en el número máximo de iteraciones
    return None

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos los nodos y las restricciones del grafo
    nodos = ['A', 'B', 'C', 'D']
    restricciones = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C')]

    # Ejecutamos el algoritmo de mínimos conflictos
    solucion = minimos_conflictos(nodos, restricciones)

    # Creamos el grafo para visualizarlo
    grafo = nx.Graph()
    grafo.add_nodes_from(nodos)
    grafo.add_edges_from(restricciones)

    # Dibujamos el grafo y mostramos la solución
    colores = []
    if solucion:
        print("Solucion encontrada:", solucion)
        colores = ['red' if solucion[nodo] == 0 else 'blue' for nodo in nodos]
    else:
        print("No se encontro solucion.")
        colores = ['gray' for nodo in nodos]

    # Dibujamos el grafo con colores según la solución
    nx.draw(grafo, with_labels=True, node_color=colores, node_size=500, font_color='white')
    plt.show()