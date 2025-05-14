# Importamos las bibliotecas necesarias
import networkx as nx  # Para trabajar con grafos
import matplotlib.pyplot as plt  # Para graficar los grafos


# Este programa implementa el algoritmo de Salto Atrás Dirigido por Conflictos para buscar un camino
# desde un nodo inicial hasta un nodo objetivo en un grafo. Utiliza la biblioteca NetworkX para
# representar y visualizar grafos, y Matplotlib para graficar los resultados. El programa incluye
# un ejemplo de grafo dirigido, realiza la búsqueda del camino y resalta el camino encontrado en
# la visualización del grafo.




# Definimos una función para realizar el algoritmo de Salto Atrás Dirigido por Conflictos
def salto_atras_conflictos(grafo, nodo_inicial, nodo_objetivo):
    """
    Esta función implementa el algoritmo de Salto Atrás Dirigido por Conflictos.
    Busca un camino desde el nodo_inicial hasta el nodo_objetivo en un grafo.

    :param grafo: El grafo representado como un diccionario de adyacencia.
    :param nodo_inicial: Nodo desde donde comienza la búsqueda.
    :param nodo_objetivo: Nodo que queremos alcanzar.
    :return: Una lista con el camino encontrado o None si no hay solución.
    """
    # Pila para realizar la búsqueda (almacena los caminos parciales)
    pila = [[nodo_inicial]]

    # Mientras haya caminos por explorar
    while pila:
        # Extraemos el último camino de la pila
        camino_actual = pila.pop()

        # Obtenemos el último nodo del camino actual
        ultimo_nodo = camino_actual[-1]

        # Si hemos llegado al nodo objetivo, devolvemos el camino
        if ultimo_nodo == nodo_objetivo:
            return camino_actual

        # Si no, exploramos los vecinos del último nodo
        for vecino in grafo[ultimo_nodo]:
            # Evitamos ciclos comprobando si el vecino ya está en el camino actual
            if vecino not in camino_actual:
                # Creamos un nuevo camino extendiendo el actual
                nuevo_camino = camino_actual + [vecino]
                # Lo añadimos a la pila para seguir explorándolo
                pila.append(nuevo_camino)

    # Si no encontramos un camino, devolvemos None
    return None

# Creamos un ejemplo de grafo como un diccionario de adyacencia
grafo_ejemplo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Definimos el nodo inicial y el nodo objetivo
nodo_inicial = 'A'
nodo_objetivo = 'F'

# Llamamos a la función para encontrar el camino
camino_encontrado = salto_atras_conflictos(grafo_ejemplo, nodo_inicial, nodo_objetivo)

# Imprimimos el resultado
print("Camino encontrado:", camino_encontrado)

# Visualizamos el grafo y el camino encontrado
grafo = nx.DiGraph(grafo_ejemplo)  # Creamos un grafo dirigido
pos = nx.spring_layout(grafo)  # Calculamos la posición de los nodos para graficar

# Dibujamos el grafo completo
nx.draw(grafo, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')

# Si encontramos un camino, lo resaltamos en el grafo
if camino_encontrado:
    # Creamos una lista de aristas (conexiones) en el camino encontrado
    aristas_camino = [(camino_encontrado[i], camino_encontrado[i + 1]) for i in range(len(camino_encontrado) - 1)]
    # Dibujamos las aristas del camino en rojo
    nx.draw_networkx_edges(grafo, pos, edgelist=aristas_camino, edge_color='red', width=2)

# Mostramos el grafo en pantalla
plt.title("Grafo y Camino Encontrado")
plt.show()