import networkx as nx

# Programa en Python: Comprobación Hacia Delante (Forward Checking)
# Este programa implementa un algoritmo de búsqueda en grafos con comprobación hacia adelante.
# La comprobación hacia adelante es una técnica utilizada para reducir el espacio de búsqueda
# al eliminar valores inconsistentes de los dominios de las variables antes de realizar asignaciones.

import matplotlib.pyplot as plt

# Función para verificar si una asignación es consistente
def es_consistente(asignacion, grafo, variable, valor):
    """
    Verifica si asignar un valor a una variable es consistente con las restricciones del grafo.
    """
    for vecino in grafo[variable]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False  # Si un vecino ya tiene el mismo valor, no es consistente
    return True

# Función de búsqueda con comprobación hacia adelante
def busqueda_con_comprobacion_hacia_adelante(grafo, variables, dominios, asignacion):
    """
    Implementa la búsqueda con comprobación hacia adelante para resolver problemas de asignación.
    """
    # Si todas las variables están asignadas, devolvemos la asignación
    if len(asignacion) == len(variables):
        return asignacion

    # Seleccionamos la siguiente variable no asignada
    for variable in variables:
        if variable not in asignacion:
            break

    # Intentamos asignar un valor del dominio de la variable
    for valor in dominios[variable]:
        if es_consistente(asignacion, grafo, variable, valor):
            # Asignamos el valor a la variable
            asignacion[variable] = valor

            # Realizamos la comprobación hacia adelante
            dominios_reducidos = {v: list(dominios[v]) for v in variables}
            for vecino in grafo[variable]:
                if vecino not in asignacion and valor in dominios_reducidos[vecino]:
                    dominios_reducidos[vecino].remove(valor)

            # Llamada recursiva con la nueva asignación y dominios reducidos
            resultado = busqueda_con_comprobacion_hacia_adelante(grafo, variables, dominios_reducidos, asignacion)
            if resultado:
                return resultado

            # Si no se encuentra solución, deshacemos la asignación
            del asignacion[variable]

    # Si no se puede asignar ningún valor, devolvemos None
    return None

# Ejemplo: Problema de coloreo de grafos
# Creamos un grafo simple
grafo = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Variables del problema (nodos del grafo)
variables = list(grafo.keys())

# Dominios de los colores (valores posibles para cada nodo)
dominios = {variable: ["Rojo", "Verde", "Azul"] for variable in variables}

# Asignación inicial vacía
asignacion = {}

# Llamamos a la función de búsqueda
solucion = busqueda_con_comprobacion_hacia_adelante(grafo, variables, dominios, asignacion)

# Mostramos la solución encontrada
print("Solución encontrada:", solucion)

# Visualizamos el grafo con la solución
G = nx.Graph()
for nodo, vecinos in grafo.items():
    for vecino in vecinos:
        G.add_edge(nodo, vecino)

# Asignamos colores a los nodos según la solución
color_map = {"Rojo": "red", "Verde": "green", "Azul": "blue"}  # Mapeo de colores
colores = [color_map[solucion[nodo]] for nodo in G.nodes()]

# Dibujamos el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=colores, node_size=500, font_color="white")
plt.show()